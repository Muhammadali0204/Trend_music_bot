from aiogram import types


def inline_list(data):
    listt = []
    for d in data:
        listt.append(types.InlineQueryResultVoice(id=d[0], voice_url=d[2], title=d[1]))
    return listt
