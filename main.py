import os
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("8278371466:AAFkLgk71BLQ-H9A6dmi3YcszSjFGfXP57w")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Salom! Men Railway’da 24/7 ishlayman!")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
