import os
import time
import base64
import tempfile
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from google import genai
from google.genai.types import GenerateContentConfig
import chromadb
from chromadb.config import Settings


app = Flask(__name__)
load_dotenv()
app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG", False)
app.config["FLASK_RUN_HOST"] = os.getenv("FLASK_RUN_HOST")
app.config["FLASK_RUN_PORT"] = os.getenv("FLASK_RUN_PORT")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
api = Api(app)
cors = CORS(app)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["ANONYMIZED_TELEMETRY"] = "False"


class RateLimiter:
    def __init__(self, requests_per_minute: int = 60, requests_per_second: int = 2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0

    def wait_if_needed(self):
        current_time = time.time()

        # Per-second rate limiting
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1.0 / self.requests_per_second):
            sleep_time = (1.0 / self.requests_per_second) - time_since_last
            time.sleep(sleep_time)

        # Per-minute rate limiting
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]

        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (current_time - self.request_times[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
                current_time = time.time()
                self.request_times = [t for t in self.request_times if current_time - t < 60]

        self.request_times.append(current_time)
        self.last_request_time = current_time


class RAGSystem:
    def __init__(self, gemini_api_key: str, db_path: str = "./chroma_db"):
        self.client = genai.Client(api_key=gemini_api_key)
        self.rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)

        # Initialize ChromaDB
        self.chroma_client = chromadb.PersistentClient(
            path=db_path,
            settings=Settings(anonymized_telemetry=False)
        )
        self.collection_name = "markdown_knowledge_base"

    def get_collection(self):
        """Get ChromaDB collection"""
        try:
            return self.chroma_client.get_collection(self.collection_name)
        except Exception as e:
            raise Exception(f"Collection not found. Please run embedding.py first. Error: {e}")

    def get_embedding(self, text: str, max_retries: int = 3) -> List[float]:
        """Get embedding with rate limiting and retry logic"""
        for attempt in range(max_retries):
            try:
                self.rate_limiter.wait_if_needed()
                result = self.client.models.embed_content(
                    model="text-embedding-004",
                    contents=text
                )
                return result.embeddings[0].values
            except Exception as e:
                if "rate limit" in str(e).lower() or "quota" in str(e).lower():
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                elif attempt == max_retries - 1:
                    raise Exception(f"Failed to get embedding after {max_retries} attempts: {e}")
                else:
                    time.sleep(1)
        raise Exception("Max retries exceeded")

    def get_image_description(self, image_base64: str) -> str:
        """Get description of base64 encoded image"""
        try:
            image_data = base64.b64decode(image_base64)

            with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
                temp_file.write(image_data)
                temp_file_path = temp_file.name

            try:
                my_file = self.client.files.upload(file=temp_file_path)

                response = self.client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[
                        my_file,
                        """Describe this image in detail. Focus on:
                        1. What is shown in the image (UI elements, code, diagrams, screenshots, etc.)
                        2. Any text content visible
                        3. The context or purpose of what's displayed
                        4. Technical details if it's a code screenshot or technical diagram
                        
                        Describe the content concisely but comprehensively."""
                    ],
                )

                return response.text
            finally:
                os.unlink(temp_file_path)

        except Exception as e:
            return f"Unable to process the provided image: {e}"

    def search_similar_content(self, query: str, n_results: int = 10) -> List[Dict[str, Any]]:
        """Search for similar content in ChromaDB"""
        collection = self.get_collection()

        # Get query embedding
        query_embedding = self.get_embedding(query)

        # Search in ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=['documents', 'metadatas', 'distances']
        )

        # Format results
        formatted_results = []
        for i, (doc, metadata, distance) in enumerate(zip(
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        )):
            # Convert distance to similarity (ChromaDB returns distances, not similarities)
            similarity = 1 - distance

            formatted_results.append({
                "content": doc,
                "metadata": metadata,
                "similarity": similarity,
                "rank": i + 1
            })

        return formatted_results

    def generate_response(self, question: str, context_results: List[Dict[str, Any]]) -> str:
        """Generate response using LLM with context"""
        # Build context from search results
        context_parts = []
        for result in context_results:
            metadata = result['metadata']
            content = result['content']

            # Create source identifier
            source_info = f"Source: {metadata.get('title', 'Unknown')}"
            if 'primary_url' in metadata:
                source_info += f" (URL: {metadata['primary_url']})"
            elif 'topic_url' in metadata:
                source_info += f" (URL: {metadata['topic_url']})"

            context_parts.append(f"{source_info}\n{content}")

        context = "\n\n---\n\n".join(context_parts)

        system_prompt = """You are a knowledgeable and helpful teaching assistant for online degree students.
                        Use only the information provided in the context to answer the question.

                        **Instructions:**
                        - Format your response using **Markdown**.
                        - Use code blocks (```) for any code or command-line instructions.
                        - Use bullet points or numbered lists for clarity where appropriate.
                        - Always provide specific, actionable answers when possible.
                        - When referencing information, mention the source if available.
                        - Include relevant URLs from the context in your response.

                        **IMPORTANT:** If the context does not contain enough information to answer the question, reply exactly with:
                        ```
                        I don't have enough information to answer this question based on the provided context.
                        ```

                        Do not attempt to guess, fabricate, or add external information not present in the context."""

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[
                    system_prompt,
                    f"Context: {context}",
                    f"Question: {question}"
                ],
                config=GenerateContentConfig(
                    max_output_tokens=1024,
                    temperature=0.3,
                    top_p=0.95,
                    top_k=40
                ),
            )
            return response.text
        except Exception as e:
            return f"I apologize, but I'm unable to generate a response at this time due to a technical issue: {e}"

    def extract_links_from_results(self, results: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Extract links from search results"""
        links = []
        seen_urls = set()

        for result in results[:10]:  # Top 5 results
            metadata = result['metadata']
            content = result['content']

            # Get URL from metadata
            url = None
            if 'primary_url' in metadata:
                url = metadata['primary_url']
            elif 'topic_url' in metadata:
                url = metadata['topic_url']
            elif 'urls' in metadata and metadata['urls']:
                url = metadata['urls'][0]

            # Avoid duplicate URLs
            if url in seen_urls:
                continue
            seen_urls.add(url)

            # Create snippet
            snippet = content[:100] + "..." if len(content) > 100 else content

            links.append({
                "url": url,
                "text": snippet
            })

        return links

    def answer_question(self, question: str, image: Optional[str] = None) -> Dict[str, Any]:
        """Main function to answer a question with optional image"""
        try:
            # Process question with optional image context
            processed_question = question
            if image:
                try:
                    image_description = self.get_image_description(image)
                    processed_question = f"{question}\n\nImage context: {image_description}"
                except Exception:
                    pass  # Continue with text-only if image processing fails

            # Search for similar content
            search_results = self.search_similar_content(processed_question)

            if not search_results:
                return {
                    "answer": "I couldn't find any relevant information in my knowledge base.",
                    "links": []
                }

            # Generate response
            response = self.generate_response(question, search_results)

            # Extract links
            links = self.extract_links_from_results(search_results)

            return {
                "answer": response,
                "links": links
            }

        except Exception as e:
            return {
                "answer": f"I apologize, but I encountered an error while processing your question: {str(e)}",
                "links": []
            }


# Global RAG system instance
rag_system = None


def get_rag_system():
    global rag_system
    if rag_system is None:
        if not GEMINI_API_KEY:
            raise Exception("GEMINI_API_KEY environment variable not set")
        rag_system = RAGSystem(GEMINI_API_KEY)
    return rag_system


class QuestionAnswerAPI(Resource):
    def post(self):
        try:
            data = request.get_json()

            if not data:
                return {"error": "No JSON data provided"}, 400

            question = data.get("question")
            image = data.get("image")

            if not question:
                return {"error": "Question is required"}, 400

            # Get RAG system and process question
            rag = get_rag_system()
            result = rag.answer_question(question, image)

            return result, 200

        except Exception as e:
            return {
                "error": f"Internal server error: {str(e)}",
                "answer": "I apologize, but I'm unable to process your question at this time.",
                "links": []
            }, 500


class HealthCheck(Resource):
    def get(self):
        try:
            rag = get_rag_system()
            collection = rag.get_collection()
            count = collection.count()

            return {
                "status": "healthy",
                "collection_exists": True,
                "document_count": count,
                "api_key_configured": bool(GEMINI_API_KEY)
            }, 200

        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "api_key_configured": bool(GEMINI_API_KEY)
            }, 500


class Hello(Resource):
    def get(self):
        return {
            "message": "Student Q&A API with ChromaDB RAG",
            "endpoints": {
                "POST /api/": "Submit a question with optional image",
                "GET /health": "Health check"
            },
            "example_request": {
                "question": "Which subject should I choose in Jan term?",
                "image": "base64_encoded_image_data_here (optional)"
            }
        }, 200


api.add_resource(Hello, "/")
api.add_resource(QuestionAnswerAPI, '/api/')
api.add_resource(HealthCheck, '/health')


if __name__ == '__main__':
    try:
        get_rag_system()
        print("RAG system initialized successfully")
    except Exception as e:
        print(f"Failed to initialize RAG system: {e}")
        print("Make sure to run embedding.py first and set GEMINI_API_KEY")

    app.run()
