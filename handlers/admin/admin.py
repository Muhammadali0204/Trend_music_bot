from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu, show_data, admin_menu, ortga
from data.config import ADMINS
from loader import dp, db_users, data, temp

@dp.message_handler(text="Admin", chat_id = ADMINS)
async def salom(msg : types.Message):
    await msg.answer(text="<b>Admin panel : </b>", reply_markup=admin_menu.menu)
    
    
@dp.message_handler(text="Ovoz qo'shish", chat_id = ADMINS)
async def ovoz_qushish(msg : types.Message, state : FSMContext):
    await msg.answer("<b>Ovoz uchun nom yuboring : </b>", reply_markup=ortga.ortga)
    await state.set_state("ovoz qo'shishda nomi")
    
    
@dp.message_handler(state="ovoz qo'shishda nomi", chat_id = ADMINS)
async def nomi(msg : types.Message, state : FSMContext):
    temp["ovoz nomi"] = msg.text
    await msg.answer("<b>Ovozni yuboring : </b>", reply_markup=ortga.ortga)
    await state.set_state("ovoz qo'shishda ovoz")
    
@dp.message_handler(state="ovoz qo'shishda ovoz", chat_id = ADMINS, content_types=types.ContentType.ANY)
async def ovoz(msg : types.Message, state : FSMContext):
    if msg.content_type == types.ContentType.VOICE:
        data.add_data(temp["ovoz nomi"], msg.voice.file_id, "Ovoz", 0)
        await msg.answer("<b>Ovoz qo'shildi ✅</b>", reply_markup=admin_menu.menu)
        await state.finish()
    else:
        await msg.answer("<b>Bu ovoz emas</b>", reply_markup=admin_menu.menu)
        await state.finish()
        



@dp.message_handler(text="Musiqa qo'shish", chat_id = ADMINS)
async def musiqa_qushish(msg : types.Message, state : FSMContext):
    await msg.answer("<b>Musiqa uchun nom yuboring : </b>", reply_markup=ortga.ortga)
    await state.set_state("musiqa qo'shishda nomi")
    
    
@dp.message_handler(state="musiqa qo'shishda nomi", chat_id = ADMINS)
async def nomi(msg : types.Message, state : FSMContext):
    temp["musiqa nomi"] = msg.text
    await msg.answer("<b>Musiqani yuboring : </b>", reply_markup=ortga.ortga)
    await state.set_state("musiqa qo'shishda musiqa")
    
@dp.message_handler(state="musiqa qo'shishda musiqa", chat_id = ADMINS, content_types=types.ContentType.ANY)
async def musiqa(msg : types.Message, state : FSMContext):
    if msg.content_type == types.ContentType.AUDIO:
        data.add_data(temp["musiqa nomi"], msg.audio.file_id, "Musiqa", 0)
        await msg.answer("<b>Musiqa qo'shildi ✅</b>", reply_markup=admin_menu.menu)
        await state.finish()
    else:
        await msg.answer("<b>Bu musiqa emas</b>", reply_markup=admin_menu.menu)
        await state.finish()