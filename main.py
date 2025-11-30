import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8246029414:AAHAaCezVforMTAdGRwCkCFAtGRX0kq0BNE"
API_KEY = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

bot = Bot(TOKEN)
dp = Dispatcher()

# Храним число для каждого пользователя
secret_numbers = {}

@dp.message(CommandStart())
async def start(msg: types.Message):
    num = random.randint(1, 10)
    secret_numbers[msg.from_user.id] = num
    await msg.answer("Я загадал число от 1 до 10. Попробуй угадать!")

@dp.message()
async def guess(msg: types.Message):
    user_id = msg.from_user.id

    if user_id not in secret_numbers:
        await start(msg)
        return

    try:
        g = int(msg.text)
    except:
        await msg.answer("Введи число")
        return

    num = secret_numbers[user_id]

    if g == num:
        await msg.answer("Правильно! Я загадал " + str(num) + ". Загадываю новое!")
        secret_numbers[user_id] = random.randint(1, 10)
    else:
        await msg.answer("Неправильно, попробуй ещё")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
