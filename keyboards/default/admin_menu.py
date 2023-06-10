from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Ovoz qo'shish"),
        ],
        [
            KeyboardButton(text="Musiqa qo'shish")
        ]
    ]
)