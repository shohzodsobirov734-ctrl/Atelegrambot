from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom! Bot 24/7 ishlayapti ✅")

executor.start_polling(dp)
