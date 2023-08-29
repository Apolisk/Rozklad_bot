from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from keyboard.inline import train_keyboard
from parcing.get_info import miski,mizmiski,primiski
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from states.choose_station import user_choose
from parcing.trains import get_road
from keyboard.default import main_menu

@dp.message_handler()
async def bus(message: types.Message):
    if message.text == "МІЖМІСЬКІ МАРШРУТИ":
        await dp.bot.send_message(chat_id=message.from_user.id, text="0", reply_markup=mizmiski())
    elif message.text == "ПРИМІСЬКІ МАРШРУТИ":
        await dp.bot.send_message(chat_id=message.from_user.id, text="1", reply_markup=primiski())
    elif message.text == "МІСЬКІ МАРШРУТИ":
        await dp.bot.send_message(chat_id=message.from_user.id, text="2", reply_markup=miski())
    elif message.text == "ЕЛЕКТРИЧКИ":
        await dp.bot.send_message(chat_id=message.from_user.id, text="3", reply_markup=train_keyboard)
        await dp.bot.send_message(chat_id=message.from_user.id, text="<b>Выберете 2 станции, нажимая на них последовательно</b>", parse_mode="html")
        
        await user_choose.first_station.set()
        
# Маршрутки
@dp.callback_query_handler(filters.Text(startswith="http://obukhivtrans.com.ua/"))
async def send_linK(call: types.CallbackQuery):
        await dp.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await call.message.answer_photo(photo=call.data, reply_markup=main_menu)   
#-----------------------------------------------------------------------
# Электрички
@dp.callback_query_handler(state=user_choose.first_station)
async def send_route(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(first=call.data)
    await user_choose.next()

@dp.callback_query_handler(state=user_choose.second_station)
async def send_route(call: types.CallbackQuery, state: FSMContext):
    
    first = await state.get_data()
    firstans = first.get("first")
    second = call.data
    await call.message.delete()
    await call.message.answer(text=f"<pre>{get_road(firstans, second)}</pre>" , parse_mode="html", reply_markup=main_menu )
    await state.finish()
