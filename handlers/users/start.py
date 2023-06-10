from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import menu
from loader import dp, db_users


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    data = db_users.select_user(msg.from_user.id)
    if data == None:
        db_users.add_user(msg.from_user.id)
        
    await msg.answer(f"<b>Assalomu alaykum, {msg.from_user.get_mention(msg.from_user.first_name)}\n\nBotimizdan trendga chiqqan qiziqarli musiqa va ovozlarni topishingiz mumkin 😄</b>", reply_markup=menu.menu)
    
    
