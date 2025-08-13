import json
from difflib import unified_diff

from langchain_core.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException  # ✅ use this
from llm_helper import llm



def extract_metadata(post):
    template = '''
You are a strict JSON generator. Given a LinkedIn post, return ONLY valid JSON with this structure:

{{
  "line_count": <number of lines in the post>,
  "language": "English" or "Hinglish",
  "tags": ["tag1", "tag2"]
}}

❌ No explanation  
❌ No extra words  
✅ Just the JSON

Here is the post:
{post}
'''

    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke({"post": post})

    print("\n🧠 LLM Response:")
    print(response.content)

    try:
        result = json.loads(response.content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned: {e}")

    return result

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []

    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        print("📄 Loaded Posts:")
        print(posts)

        for post in posts:
            try:
                metadata = extract_metadata(post['Text'])  # assumes post has a 'Text' key
                post_with_metadata = post | metadata
                enriched_posts.append(post_with_metadata)
            except Exception as e:
                print(f"❌ Failed to process post: {post.get('Text', '')[:50]}...\nReason: {e}")

    with open(processed_file_path, 'w', encoding='utf-8') as out_file:
        json.dump(enriched_posts, out_file, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved {len(enriched_posts)} enriched posts to {processed_file_path}")


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
