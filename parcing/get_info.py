import requests
from bs4 import BeautifulSoup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


r = requests.get("http://obukhivtrans.com.ua/rozklad.html",  )
r.encoding = 'utf-8'
data = BeautifulSoup(r.text, "lxml")

a={}
table = data.find_all(class_="imB0")
for i in range(len(table)):
    a[i] = table[i]


def miski():
    miksi_keyboard = InlineKeyboardMarkup(row_width=2)
    miski = a[0].find_all("a")
    for i in miski:
        i_url = i.get("href")
        miksi_keyboard.insert(InlineKeyboardButton(text=f"{i.text}", callback_data=f"http://obukhivtrans.com.ua/{i_url}"))
    return miksi_keyboard


def primiski():
    primiski_keyboard = InlineKeyboardMarkup(row_width=2)
    primiski = a[1].find_all("a")
    for i in primiski:
        i_url = i.get("href")
        primiski_keyboard.insert(InlineKeyboardButton(text=f"{i.text}", callback_data=f"http://obukhivtrans.com.ua/{i_url}"))
    return primiski_keyboard


def mizmiski():
    mizmiksi_keyboard = InlineKeyboardMarkup(row_width=2)
    mizmiski = a[2].find_all("a")
    for i in mizmiski:
        i_url = i.get("href")
        mizmiksi_keyboard.insert(InlineKeyboardButton(text=f"{i.text}", callback_data=f"http://obukhivtrans.com.ua/{i_url}"))
    return mizmiksi_keyboard
