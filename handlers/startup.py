from aiogram import types
from loader import dp
from keyboard.default import main_menu
from bd.add_user import reg_check_user
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await dp.bot.send_message(chat_id=message.from_user.id, text="Hello", reply_markup=main_menu)
    user = message.from_user.first_name
    user_id = message.from_user.id
    reg_check_user(user_name=user, user_id=user_id)