OPENAI_API_KEY = "sk-abcdqrstefgh5678abcdqrstefgh5678abcdqrst"

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("AI Text Completion Tool. Type 'exit' to quit.")
    while True:
        prompt = input("\nEnter your prompt: ")
        if prompt.lower() == 'exit':
            break
        if not prompt.strip():
            print("Prompt cannot be empty!")
            continue
        response = get_completion(prompt)
        print("\nResponse:\n", response)

if __name__ == "__main__":
    main()