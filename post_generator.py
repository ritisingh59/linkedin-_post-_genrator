from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    elif length == "Long":
        return "11 to 15 lines"
    else:
        return "Custom length"

def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f"""Generate a LinkedIn post using the below information. No Preamble.

1) Topic: {tag}
2) Length: {length_str}
3) Language: {language}
"""

    examples = few_shot.get_filtered_posts(length, language, tag)
    if len(examples) > 0:
        prompt += "\n4) Use the writing style as per the following examples:\n"
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\nExample {i+1}:\n{post_text.strip()}\n"
            if i == 1:  # only include up to 2 examples
                break
    return prompt.strip()

def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)

    # 📩 Print the prompt being sent to the LLM
    print("📩 Prompt Sent to LLM:\n")
    print(prompt)
    print("\n" + "="*60 + "\n")

    # ✅ Generate response
    response = llm.invoke(prompt)
    print("✅ Generated LinkedIn Post:\n")
    print(response.content)

if __name__ == "__main__":
    generate_post("Short", "English", "Job Search")
