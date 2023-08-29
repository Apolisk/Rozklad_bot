from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(token="Your Token Here")

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)