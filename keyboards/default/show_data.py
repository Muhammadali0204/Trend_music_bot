from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def show_data(data):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.insert(KeyboardButton(text="⬅️Ortga"))
    for d in data:
        keyboard.insert(KeyboardButton(text=d[1]))

    keyboard.insert(KeyboardButton(text="⬅️Ortga"))

    return keyboard
