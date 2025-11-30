import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8246029414:AAHAaCezVforMTAdGRwCkCFAtGRX0kq0BNE"
API_KEY = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true
"

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Напиши город")

@dp.message()
async def weather(msg: types.Message):
    city = msg.text.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            data = await r.json()

    if data.get("cod") != 200:
        await msg.answer("Город не найден")
        return

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    await msg.answer(f"{city}: {temp}°C, {desc}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
