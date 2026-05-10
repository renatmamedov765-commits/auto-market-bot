import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from config import TOKEN, ADMIN_ID
from db import init_db, add_car, get_cars, add_request
from keyboards import main_menu, car_kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

# START
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🚗 Добро пожаловать в авто-маркетплейс",
        reply_markup=main_menu()
    )


# КАТАЛОГ
@dp.callback_query(F.data == "catalog")
async def catalog(call: types.CallbackQuery):
    cars = await get_cars()

    if not cars:
        await call.message.answer("🚫 Пока нет авто")
        return

    for car in cars:
        car_id, title, price, desc = car

        text = f"""
🚗 {title}
💰 {price}

📝 {desc}
        """

        await call.message.answer(text, reply_markup=car_kb(car_id))


# ДОБАВИТЬ АВТО (админ)
@dp.message(F.text.startswith("/addcar"))
async def addcar(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        _, title, price, desc = message.text.split("|")
        await add_car(title.strip(), price.strip(), desc.strip())
        await message.answer("✅ Авто добавлено")
    except:
        await message.answer("Формат:\n/addcar | BMW E46 | 450000 | Описание")


# ЗАЯВКА
@dp.callback_query(F.data.startswith("req_"))
async def request(call: types.CallbackQuery):
    car_id = int(call.data.split("_")[1])

    await call.message.answer("📞 Отправь контакт или Telegram username")

    @dp.message()
    async def save_contact(message: types.Message):
        await add_request(message.from_user.username, car_id, message.text)
        await message.answer("✅ Заявка отправлена")


async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
