import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

cars = [
    {"title": "BMW E46", "price": "450 000 ₽", "desc": "Живой кузов"}
]

@dp.message(CommandStart())
async def start(message: types.Message):
    text = "🚗 Каталог авто:\n\n"
    for car in cars:
        text += f"{car['title']} — {car['price']}\n{car['desc']}\n\n"

    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
