from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api import sqlite

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_users = sqlite.Database("data/Users.db")
data = sqlite.Database("data/Data.db")
try : 
    db_users.create_table_users()
except :
    pass

try : 
    data.create_table_data()
except :
    pass

temp = {}




