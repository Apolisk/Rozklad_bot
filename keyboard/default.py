from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


main_menu = ReplyKeyboardMarkup(keyboard = 
    [
        [
            KeyboardButton(text="МІСЬКІ МАРШРУТИ"),
            KeyboardButton(text="ПРИМІСЬКІ МАРШРУТИ")
        ],

        [
            KeyboardButton(text="МІЖМІСЬКІ МАРШРУТИ"),
            KeyboardButton(text="ЕЛЕКТРИЧКИ") 
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True)