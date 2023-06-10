from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu, show_data

from loader import dp, db_users, data


@dp.message_handler(text="🔊Ovozlar")
async def ovozlar(msg : types.Message, state : FSMContext):
    ovozlar1 = data.select_data_turi_ordered("Ovoz")
    
    if ovozlar == []:
        await msg.answer("<b>Ovozlar mavjud emas !</b>", reply_markup=menu.menu)
    else:
        await msg.answer("<b>🔊Ovozlar</b>", reply_markup=show_data.show_data(ovozlar1))
        await state.set_state("ovozlar")

@dp.message_handler(text="⬅️Ortga",state=["ovozlar", "top", "qidirish", "qidiruv natijasi"])
async def ovoz_ortga(msg : types.Message, state : FSMContext):
    await msg.answer("<b>Menu : </b>", reply_markup=menu.menu)
    await state.finish()

@dp.message_handler(state="ovozlar")
async def ovoz_junatish(msg : types.Message):
    ovoz = data.select_data_nom(msg.text)
    if ovoz != None:
        await msg.answer_voice(ovoz[2], caption=ovoz[1])
        data.update_status(ovoz[0], (ovoz[4] + 1))
    else:
        ovozlar = data.select_data_turi_ordered("Ovoz")
        await msg.answer("<b>Quyidagi ro'yxatdan foydalaning 👇</b>", reply_markup=show_data.show_data(ovozlar))
    