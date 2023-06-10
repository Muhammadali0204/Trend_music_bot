from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu, show_data

from loader import dp, db_users, data

@dp.message_handler(text="🟢TOP 10")
async def top10(msg : types.Message, state : FSMContext):
    data_top = data.select_top()
    if len(data_top) > 10:
        data_top = data.select_top()[:10]
    await msg.answer("<b>🟢TOP 10</b>", reply_markup=show_data.show_data(data_top))
    await state.set_state("top")
    
    
@dp.message_handler(state="top")
async def ovoz_junatish(msg : types.Message):
    ovoz = data.select_data_nom(msg.text)
    if ovoz != None:
        await msg.answer_voice(ovoz[2], caption=ovoz[1])
        data.update_status(ovoz[0], (ovoz[4] + 1))
    else:
        data_top = data.select_top()
        if len(data_top) > 10:
            data_top = data.select_top()[:10]
        await msg.answer("<b>Quyidagi ro'yxatdan foydalaning 👇</b>", reply_markup=show_data.show_data(data_top))