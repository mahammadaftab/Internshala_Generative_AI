import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import openai

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not BOT_TOKEN:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN environment variable.")

if not OPENROUTER_API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY environment variable.")

openai.api_base = "https://openrouter.ai/v1"
openai.api_key = OPENROUTER_API_KEY

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def welcome(message: types.Message):
    await message.reply(
        "Hello! I am GPT Chat BOT. 😊\n"
        "You can ask me anything, and I’ll do my best to help."
    )

@dp.message()
async def gpt_reply(message: types.Message):
    prompt_messages = [
        {"role": "system", "content": "You are a friendly and helpful assistant."},
        {"role": "user", "content": message.text}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt_messages,
            max_tokens=250,
            temperature=0.7
        )
        answer = response.choices[0].message.content.strip()
        await message.reply(answer)
    except Exception as error:
        await message.reply(
            "Sorry, I couldn't process that request right now. Please try again later."
        )
        raise

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
