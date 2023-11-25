from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu, show_data

from loader import dp, db_users, data


@dp.message_handler(text="🤖Bot haqida")
async def bot_haqida(msg: types.Message):
    n = db_users.count_users()
    answer = f"<b>Bot foydalanuvchilari soni : </b><i>{n[0]} ta</i>\n"
    n = data.count_users_data()
    answer += f"<b>Botda mavjud musiqa va ovozlar soni : </b><i>{n[0]} ta</i>\n\n"
    answer += "<b>Inline mode'ni qo'llab quvvatlaydi ✅</b>\n<i>Ya'ni istalgan chatda turib @trend_music_bot deb yozing va kerak bo'lgan ovoz yoki musiqani nomini kiriting.\n</i>"
    answer += "\n<b>👨‍💻Admin : <i>@javob_tekshir_admin_bot</i>\n\n🤖Boshqa botlarimiz : \n<i>1. @javob_tekshir_bot\n2. @dtmtests_bot</i></b>"
    await msg.answer(answer, reply_markup=menu.menu)
