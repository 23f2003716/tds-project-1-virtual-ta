import io
import json
import os
import re
import time
import requests
import google.genai as genai
from pathlib import Path
from typing import Dict, List, Any, Optional
from html import unescape
from google.genai.types import GenerateContentConfig
from PIL import Image
from dotenv import load_dotenv


class DiscoursePreprocessor:
    def __init__(self, gemini_api_key: str):
        self.gemini_api_key = gemini_api_key
        self.client = genai.Client(api_key=gemini_api_key)

        # Fields to keep from the main topic
        self.topic_fields = {
            'id', 'title', 'created_at', 'views', 'reply_count',
            'like_count', 'tags', 'category_id', 'slug'
        }

        # Fields to keep from posts
        self.post_fields = {
            'id', 'name', 'username', 'created_at', 'cooked',
            'post_number', 'reply_count', 'quote_count', 'reads',
            'score', 'topic_id', 'display_username', 'user_title'
        }

        # Emoji URL patterns to exclude
        self.emoji_patterns = [
            r'https://emoji\.discourse-cdn\.com/',
            r'emoji\.discourse-cdn\.com',
            r'/images/emoji/',
            r'\.discourse-cdn\.com/.*emoji',
        ]

    def is_emoji_image(self, url: str) -> bool:
        """Check if the URL points to an emoji image"""
        if not url:
            return False
        
        # Check against emoji patterns
        for pattern in self.emoji_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return True
        
        # Check for common emoji file naming patterns
        emoji_file_patterns = [
            r':\w+:',  # :white_check_mark: style
            r'emoji.*\.(png|gif|svg|jpg|jpeg)$',
            r'\.(png|gif|svg).*emoji',
        ]
        
        for pattern in emoji_file_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return True
        
        return False

    def clean_topic_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Extract main topic info
        topic_info = {k: v for k, v in data.items() if k in self.topic_fields}

        # Clean posts
        if 'post_stream' in data and 'posts' in data['post_stream']:
            cleaned_posts = []
            for post in data['post_stream']['posts']:
                cleaned_post = {k: v for k, v in post.items() if k in self.post_fields}
                cleaned_posts.append(cleaned_post)

            topic_info['posts'] = cleaned_posts

        return topic_info

    def download_image(self, url: str) -> Optional[Image.Image]:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            image = Image.open(io.BytesIO(response.content))
            return image
        except Exception as e:
            print(f"Error downloading image {url}: {e}")
            return None

    def get_image_description(self, image_url: str):
        try:
            # Download the image
            image = self.download_image(image_url)
            if not image:
                return "[Image could not be loaded for description]"

            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Convert PIL Image to bytes for the new API
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # Generate description using Gemini
            prompt = """Describe this image in detail. Focus on:
            1. What is shown in the image (UI elements, code, diagrams, screenshots, etc.)
            2. Any text content visible
            3. The context or purpose of what's displayed
            4. Technical details if it's a code screenshot or technical diagram
            
            Describe the content of this image in detail, focusing on any text, objects, or relevant features that could help answer questions about it."""

            # Create the request using the new API
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents=[
                    {
                        'parts': [
                            {'text': prompt},
                            {
                                'inline_data': {
                                    'mime_type': 'image/png',
                                    'data': img_byte_arr
                                }
                            }
                        ]
                    }
                ],
                config=GenerateContentConfig(
                    temperature=0.1,
                    max_output_tokens=500
                )
            )

            # Add a small delay to avoid rate limiting
            time.sleep(1)

            return response.text

        except Exception as e:
            print(f"Error getting description for image {image_url}: {e}")
            return f"[Image description unavailable: {str(e)}]"

    def process_html_content(self, html_content: str) -> str:
        if not html_content:
            return ""

        # Find all image elements in lightbox wrappers
        lightbox_pattern = r'<div class="lightbox-wrapper">.*?<a class="lightbox" href="([^"]+)".*?<img src="([^"]+)" alt="([^"]*)".*?</div>'

        def replace_image(match):
            full_img_url = match.group(1)
            thumb_url = match.group(2)
            alt_text = match.group(3)

            # Check if this is an emoji image
            if self.is_emoji_image(full_img_url) or self.is_emoji_image(thumb_url):
                print(f"Skipping emoji image: {alt_text or full_img_url}")
                # Return the alt text or a generic emoji placeholder
                emoji_text = alt_text if alt_text else "emoji"
                return f" {emoji_text} "

            print(f"Processing image: {alt_text or 'Untitled'}")

            # Get description from Gemini
            description = self.get_image_description(full_img_url)

            # Format as markdown with description
            return f"\n\n**Image: {alt_text or 'Screenshot'}**\n{description}\n\n"

        # Replace lightbox images
        processed = re.sub(lightbox_pattern, replace_image, html_content, flags=re.DOTALL)

        # Handle simple img tags
        img_pattern = r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>'

        def replace_simple_img(match):
            img_url = match.group(1)
            alt_text = match.group(2)

            # Check if this is an emoji image
            if self.is_emoji_image(img_url):
                print(f"Skipping emoji image: {alt_text or img_url}")
                # Return the alt text or a generic emoji placeholder
                emoji_text = alt_text if alt_text else "emoji"
                return f" {emoji_text} "

            print(f"Processing simple image: {alt_text or 'Untitled'}")

            description = self.get_image_description(img_url)
            return f"\n\n**Image: {alt_text or 'Image'}**\n{description}\n\n"

        processed = re.sub(img_pattern, replace_simple_img, processed)

        # Clean up HTML tags and convert to markdown-like format
        processed = re.sub(r'<p>', '\n', processed)
        processed = re.sub(r'</p>', '\n', processed)
        processed = re.sub(r'<br\s*/?>', '\n', processed)
        processed = re.sub(r'<strong>(.*?)</strong>', r'**\1**', processed)
        processed = re.sub(r'<em>(.*?)</em>', r'*\1*', processed)
        processed = re.sub(r'<code>(.*?)</code>', r'`\1`', processed)
        processed = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', processed)

        # Remove remaining HTML tags
        processed = re.sub(r'<[^>]+>', '', processed)

        # Decode HTML entities
        processed = unescape(processed)

        # Clean up extra whitespace
        processed = re.sub(r'\n\s*\n\s*\n', '\n\n', processed)
        processed = processed.strip()

        return processed

    def generate_post_url(self, topic_slug: str, topic_id: int, post_number: int) -> str:
        """Generate the post URL using the Discourse URL format"""
        return f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_slug}/{topic_id}/{post_number}"

    def convert_to_markdown(self, topic_data: Dict[str, Any]) -> str:
        markdown_lines = []

        # Topic header
        title = topic_data.get('title', 'Untitled')
        topic_id = topic_data.get('id', 0)
        topic_slug = topic_data.get('slug', 'untitled')

        markdown_lines.append(f"# {title}")
        markdown_lines.append("")

        # Add topic URL (first post URL)
        topic_url = self.generate_post_url(topic_slug, topic_id, 1)
        markdown_lines.append(f"**Topic URL**: {topic_url}")
        markdown_lines.append("")

        # Metadata
        markdown_lines.append("## Topic Metadata")
        markdown_lines.append(f"- **ID**: {topic_id}")
        markdown_lines.append(f"- **Slug**: {topic_slug}")
        markdown_lines.append(f"- **Created**: {topic_data.get('created_at', 'N/A')}")
        markdown_lines.append(f"- **Views**: {topic_data.get('views', 0)}")
        markdown_lines.append(f"- **Replies**: {topic_data.get('reply_count', 0)}")
        markdown_lines.append(f"- **Likes**: {topic_data.get('like_count', 0)}")

        if topic_data.get('tags'):
            tags = ', '.join(topic_data['tags'])
            markdown_lines.append(f"- **Tags**: {tags}")

        markdown_lines.append("")

        # Posts
        posts = topic_data.get('posts', [])
        for i, post in enumerate(posts):
            post_number = post.get('post_number', i + 1)

            if i == 0:
                markdown_lines.append("## Original Post")
            else:
                markdown_lines.append(f"## Reply {i}")

            # Post metadata with URL
            author = post.get('display_username') or post.get('name') or post.get('username', 'Unknown')
            created_at = post.get('created_at', 'N/A')
            post_url = self.generate_post_url(topic_slug, topic_id, post_number)

            markdown_lines.append(f"**Author**: {author}")
            markdown_lines.append(f"**Posted**: {created_at}")
            markdown_lines.append(f"**Post URL**: {post_url}")
            markdown_lines.append("")

            # Process post content
            content = post.get('cooked', '')
            processed_content = self.process_html_content(content)

            if processed_content:
                markdown_lines.append(processed_content)
            else:
                markdown_lines.append("*No content*")

            markdown_lines.append("")
            markdown_lines.append("---")
            markdown_lines.append("")

        return '\n'.join(markdown_lines)

    def process_json_file(self, input_path: str, output_dir: str) -> str:
        # Load JSON data
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Clean the data
        cleaned_data = self.clean_topic_data(data)

        # Convert to markdown
        markdown_content = self.convert_to_markdown(cleaned_data)

        # Create output filename
        topic_id = cleaned_data.get('id', 'unknown')
        slug = cleaned_data.get('slug', 'untitled')
        output_filename = f"{topic_id}_{slug}.md"
        output_path = os.path.join(output_dir, output_filename)

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"Processed: {input_path} -> {output_path}")
        return output_path

    def process_directory(self, input_dir: str, output_dir: str) -> List[str]:
        input_path = Path(input_dir)
        json_files = list(input_path.glob("*.json"))

        if not json_files:
            print(f"No JSON files found in {input_dir}")
            return []

        processed_files = []

        for json_file in json_files:
            try:
                output_path = self.process_json_file(str(json_file), output_dir)
                processed_files.append(output_path)
            except Exception as e:
                print(f"Error processing {json_file}: {e}")

        return processed_files


if __name__ == "__main__":
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    INPUT_JSON_DIR = "downloaded_threads"
    OUTPUT_DIR = "markdown_discourse"

    preprocessor = DiscoursePreprocessor(GEMINI_API_KEY)

    try:
        processed_files = preprocessor.process_directory(INPUT_JSON_DIR, OUTPUT_DIR)
        print(f"Processed {len(processed_files)} files")
    except Exception as e:
        print(f"Error: {e}")
