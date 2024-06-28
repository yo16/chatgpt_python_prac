import os
import asyncio
from dotenv import load_dotenv

from openai import AsyncOpenAI

async def main(client) -> None:
    chat_completion = await client.chat.completions.create(
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "こんにちは、今日はどんな天気ですか？"}
        ],
        model="gpt-3.5-turbo"
    )

    print(chat_completion.choices[0].message.content)


if __name__=="__main__":
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = AsyncOpenAI(
        api_key=api_key
    )

    asyncio.run(main(client))

