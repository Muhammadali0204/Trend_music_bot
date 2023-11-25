from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import admin_menu, ortga
from data.config import ADMINS
from loader import dp


@dp.message_handler(
    text="⬅️Ortga",
    state=[
        "ovoz qo'shishda nomi",
        "ovoz qo'shishda ovoz",
        "reklama_turi",
        "copy",
        "forward",
    ],
    chat_id=ADMINS,
)
async def nomi(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer("<b>Admin menu : </b>", reply_markup=admin_menu.menu)
