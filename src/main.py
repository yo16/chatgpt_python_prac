import os
from dotenv import load_dotenv

from openai import OpenAI

def main():
    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(
        api_key=api_key
    )

    chat_completion = client.chat.completions.create(
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "こんにちは、今日はどんな天気ですか？"}
        ],
        model="gpt-3.5-turbo"
    )

    print(chat_completion['choices'][0]['message']['content'])


if __name__=="__main__":
    load_dotenv()

    main()
