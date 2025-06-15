import chromadb
import hashlib
import markdown
import os
import re
import time
from bs4 import BeautifulSoup
from chromadb.config import Settings
from dotenv import load_dotenv
from google import genai
from pathlib import Path
from typing import List, Dict, Any

load_dotenv()


class MarkdownProcessor:
    def __init__(self, gemini_api_key: str):
        self.client = genai.Client(api_key=gemini_api_key)
        self.rate_limiter = RateLimiter()

    def chunk_markdown_content(self, content: str, chunk_size: int = 5000, overlap: int = 500) -> List[str]:
        """Split markdown content into overlapping chunks while preserving structure"""
        # Convert markdown to HTML to better understand structure
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')

        # Extract text while preserving some structure markers
        text = soup.get_text()

        # Split into sentences for better chunking
        sentences = re.split(r'(?<=[.!?])\s+', text)

        chunks = []
        current_chunk = ""

        for sentence in sentences:
            # If adding this sentence would exceed chunk size, save current chunk
            if len(current_chunk) + len(sentence) > chunk_size and current_chunk:
                chunks.append(current_chunk.strip())
                # Start new chunk with overlap from previous chunk
                words = current_chunk.split()
                overlap_words = words[-overlap:] if len(words) > overlap else words
                current_chunk = " ".join(overlap_words) + " " + sentence
            else:
                current_chunk += " " + sentence if current_chunk else sentence

        # Add the last chunk
        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks

    def extract_metadata_from_markdown(self, content: str, filepath: str) -> Dict[str, Any]:
        """Extract metadata from markdown file"""
        metadata = {
            "file_path": str(filepath),
            "file_name": Path(filepath).name,
        }

        # Extract URLs from content
        urls = re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+', content)
        if urls:
            # Store URLs as comma-separated string instead of list
            metadata["urls"] = ", ".join(urls)
            metadata["primary_url"] = urls[0]  # Use first URL as primary
            metadata["url_count"] = len(urls)  # Store count as integer

        # Extract title from markdown
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata["title"] = title_match.group(1).strip()
        else:
            metadata["title"] = Path(filepath).stem.replace('-', ' ').title()

        # Extract topic metadata if present (from discourse format)
        topic_url_match = re.search(r'\*\*Topic URL\*\*:\s*(https?://[^\s]+)', content)
        if topic_url_match:
            metadata["topic_url"] = topic_url_match.group(1)
            metadata["source_type"] = "discourse"
        else:
            metadata["source_type"] = "documentation"

        return metadata

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
                    print(f"Rate limit hit, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                elif attempt == max_retries - 1:
                    raise Exception(f"Failed to get embedding after {max_retries} attempts: {e}")
                else:
                    print(f"Attempt {attempt + 1} failed: {e}, retrying...")
                    time.sleep(1)
        raise Exception("Max retries exceeded")

    def process_markdown_files(self, directories: List[str]) -> List[Dict[str, Any]]:
        """Process all markdown files in specified directories"""
        processed_docs = []
        md_files = []
        for directory in directories:
            dir_path = Path(directory)
            if dir_path.exists() and dir_path.is_dir():
                dir_md_files = list(dir_path.glob("*.md"))
                md_files.extend(dir_md_files)
                print(f"Found {len(dir_md_files)} markdown files in {directory}")
            else:
                print(f"Warning: Directory {directory} does not exist or is not a directory")

        print(f"Total: {len(md_files)} markdown files to process")

        for filepath in md_files:
            try:
                print(f"Processing: {filepath}")

                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract metadata
                metadata = self.extract_metadata_from_markdown(content, filepath)

                # Create chunks
                chunks = self.chunk_markdown_content(content)
                print(f"Created {len(chunks)} chunks")

                # Process each chunk
                for i, chunk in enumerate(chunks):
                    if len(chunk.strip()) < 50:  # Skip very short chunks
                        continue

                    try:
                        embedding = self.get_embedding(chunk)

                        doc_data = {
                            "id": self._generate_chunk_id(filepath, i),
                            "content": chunk,
                            "embedding": embedding,
                            "metadata": {
                                **metadata,
                                "chunk_index": i,
                                "chunk_count": len(chunks)
                            }
                        }
                        processed_docs.append(doc_data)

                    except Exception as e:
                        print(f"Error processing chunk {i}: {e}")
                        continue

            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                continue

        return processed_docs

    def _generate_chunk_id(self, filepath: Path, chunk_index: int) -> str:
        """Generate unique ID for chunk"""
        content = f"{filepath.name}_{chunk_index}"
        return hashlib.md5(content.encode()).hexdigest()


class RateLimiter:
    def __init__(self, requests_per_minute: int = 1500, requests_per_second: int = 5):
        """
        Rate limiter for text-embedding-004 model
        Default limits: 1500 requests per minute, 5 requests per second
        """
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


class ChromaDBManager:
    def __init__(self, db_path: str = "./chroma_db"):
        # Disable telemetry
        os.environ["ANONYMIZED_TELEMETRY"] = "False"

        self.client = chromadb.PersistentClient(
            path=db_path,
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        self.collection_name = "markdown_knowledge_base"

    def get_or_create_collection(self):
        """Get or create ChromaDB collection"""
        try:
            collection = self.client.get_collection(self.collection_name)
            print(f"Using existing collection: {self.collection_name}")
        except:
            collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "RAG knowledge base for markdown documents"}
            )
            print(f"Created new collection: {self.collection_name}")

        return collection

    def add_documents(self, documents: List[Dict[str, Any]]):
        """Add documents to ChromaDB"""
        if not documents:
            print("No documents to add")
            return

        collection = self.get_or_create_collection()

        # Prepare data for ChromaDB
        ids = [doc["id"] for doc in documents]
        contents = [doc["content"] for doc in documents]
        embeddings = [doc["embedding"] for doc in documents]
        metadatas = [doc["metadata"] for doc in documents]

        # Validate metadata before adding
        for i, metadata in enumerate(metadatas):
            validated_metadata = self._validate_metadata(metadata)
            metadatas[i] = validated_metadata

        # Add to collection in batches to avoid memory issues
        batch_size = 100
        for i in range(0, len(documents), batch_size):
            batch_end = min(i + batch_size, len(documents))

            collection.add(
                ids=ids[i:batch_end],
                documents=contents[i:batch_end],
                embeddings=embeddings[i:batch_end],
                metadatas=metadatas[i:batch_end]
            )

            print(f"Added batch {i//batch_size + 1}: {batch_end - i} documents")

        print(f"Successfully added {len(documents)} documents to ChromaDB")

    def _validate_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and clean metadata for ChromaDB compatibility"""
        validated = {}
        for key, value in metadata.items():
            if isinstance(value, (str, int, float, bool)) or value is None:
                validated[key] = value
            elif isinstance(value, list):
                # Convert lists to comma-separated strings
                validated[key] = ", ".join(str(item) for item in value)
            elif isinstance(value, dict):
                # Convert dicts to JSON strings
                import json
                validated[key] = json.dumps(value)
            else:
                # Convert other types to strings
                validated[key] = str(value)
        return validated

    def reset_collection(self):
        """Reset the collection (delete all data)"""
        try:
            self.client.delete_collection(self.collection_name)
            print(f"Deleted existing collection: {self.collection_name}")
        except:
            pass

    def get_collection_info(self):
        """Get information about the collection"""
        try:
            collection = self.client.get_collection(self.collection_name)
            count = collection.count()
            return {"count": count, "exists": True}
        except:
            return {"count": 0, "exists": False}


def main():
    # Check environment variables
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY environment variable not set")
        return

    # Configuration
    markdown_directories = ["markdown_discourse", "tds_markdown_files"]
    reset_database = input("Reset database? (y/N): ").lower() == 'y'

    # Initialize components
    chroma_manager = ChromaDBManager()
    processor = MarkdownProcessor(gemini_api_key)

    # Reset database if requested
    if reset_database:
        chroma_manager.reset_collection()

    # Check current state
    info = chroma_manager.get_collection_info()
    print(f"Current collection state: {info['count']} documents")

    if info['count'] > 0 and not reset_database:
        proceed = input("Collection already has data. Continue adding? (y/N): ").lower() == 'y'
        if not proceed:
            print("Exiting...")
            return

    # Process markdown files from specified directories
    print("Processing markdown files...")
    processed_docs = processor.process_markdown_files(markdown_directories)

    if not processed_docs:
        print("No documents were processed successfully")
        return

    # Add to ChromaDB
    print(f"\nAdding {len(processed_docs)} processed chunks to ChromaDB...")
    chroma_manager.add_documents(processed_docs)

    # Final status
    final_info = chroma_manager.get_collection_info()
    print(f"\nEmbedding complete! Total documents in collection: {final_info['count']}")


if __name__ == "__main__":
    main()
