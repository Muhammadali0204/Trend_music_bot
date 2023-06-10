from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu, show_data

from loader import dp, db_users, data


@dp.message_handler(text="🎵Musiqalar")
async def musiqalarr(msg : types.Message, state : FSMContext):
    musiqalar = data.select_data_turi_ordered("Musiqa")
    
    if musiqalar == []:
        await msg.answer("<b>Musiqalar mavjud emas !</b>", reply_markup=menu.menu)
    else:
        await msg.answer("<b>🎵Musiqalar</b>", reply_markup=show_data.show_data(musiqalar))
        await state.set_state("musiqalar")

@dp.message_handler(text="⬅️Ortga",state="musiqalar")
async def musiqa_ortga(msg : types.Message, state : FSMContext):
    await msg.answer("<b>Menu : </b>", reply_markup=menu.menu)
    await state.finish()

@dp.message_handler(state="musiqalar")
async def musiqa_junatish(msg : types.Message):
    musiqa = data.select_data_nom(msg.text)
    if musiqa != None:
        await msg.answer_audio(musiqa[2], caption=musiqa[1])
        data.update_status(musiqa[0], (musiqa[4] + 1))
    else:
        musiqalar = data.select_data_turi_ordered("Musiqa")
        await msg.answer("<b>Quyidagi ro'yxatdan foydalaning 👇</b>", reply_markup=show_data.show_data(musiqalar))