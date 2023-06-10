from aiogram import types
from keyboards.inline import inline_query


from loader import dp, db_users, data



@dp.inline_handler()
async def inline_query1(query : types.InlineQuery):
    text = query.query
    print(text)
    if text != None:
        ovozlar = data.select_data_nomlar(text)
        if ovozlar == []:
            print("2")
            pass
        else:
            await query.answer(inline_query.inline_list(ovozlar))
            print("3")