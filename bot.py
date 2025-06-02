import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
import os

API_TOKEN = os.getenv("API_TOKEN")
USER_ID = int(os.getenv("USER_ID", 0))

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
loop = asyncio.get_event_loop()

async def scheduled_messages():
    await bot.send_message(USER_ID, "🎉 Доброе утро! Сегодня ты в игре. Жди задания и комплименты весь день ❤️")
    await asyncio.sleep(60)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    if message.from_user.id == USER_ID:
        await message.reply("Привет! Я готов к бою. Жди сюрпризов 😉")

async def main():
    loop.create_task(scheduled_messages())
    await dp.start_polling()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop.run_until_complete(main())