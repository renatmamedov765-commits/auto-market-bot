from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MANAGER_USERNAME

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚗 Каталог авто", callback_data="catalog")]
    ])


def car_kb(car_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📲 Связаться с менеджером",
                url=f"https://t.me/{MANAGER_USERNAME.replace('@','')}"
            )
        ],
        [
            InlineKeyboardButton(
                text="📝 Оставить заявку",
                callback_data=f"req_{car_id}"
            )
        ]
    ])
