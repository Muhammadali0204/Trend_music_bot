from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎵Musiqalar"),
            KeyboardButton(text="🔊Ovozlar")
        ],
        [
            KeyboardButton(text="🟢TOP 10"),
            KeyboardButton(text="🔎Qidirish")
        ],
        [
            KeyboardButton(text="🤖Bot haqida")
        ]
    ], resize_keyboard=True
)