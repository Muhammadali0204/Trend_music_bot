from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu, show_data, ortga

from loader import dp, db_users, data


@dp.message_handler(text="🔎Qidirish")
async def qidieish(msg: types.Message, state: FSMContext):
    await msg.answer(
        "<b>Qidirish uchun biror so'z yuboring : </b>", reply_markup=ortga.ortga
    )
    await state.set_state("qidirish")


@dp.message_handler(state="qidirish")
async def qidir(msg: types.Message, state: FSMContext):
    if msg.text.isalpha():
        natija = data.select_data_nomlar(msg.text)
        if natija == []:
            await msg.answer(
                "<b>Hech nima topilmadi </b>🫤\n\n<i>Qayta urinib ko'ring : </i>",
                reply_markup=ortga.ortga,
            )
        else:
            await msg.answer(
                "<b>Topilgan natija(lar) : </b>",
                reply_markup=show_data.show_data(natija),
            )
            await state.set_state("qidiruv natijasi")
    else:
        await msg.answer(
            "<b>Hech nima topilmadi </b>🫤\n\n<i>Qayta urinib ko'ring : </i>",
            reply_markup=ortga.ortga,
        )


@dp.message_handler(state="qidiruv natijasi")
async def ovoz_junatish(msg: types.Message):
    ovoz = data.select_data_nom(msg.text)
    if ovoz != None:
        await msg.answer_voice(ovoz[2])
        data.update_status(ovoz[0], (ovoz[4] + 1))
