from aiogram import Dispatcher


async def on_startup(dp: Dispatcher):
    await dp.bot.send_message(chat_id=275291286, text="Up!")