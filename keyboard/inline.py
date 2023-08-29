from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

title = ['Мироновка', 'Пустовиты', 'Галино', 'Кагарлык', '71 Км Остановочный Пункт', 'Расава', 'Лозы', 'Зирки', 'Озерный', 'Гордынь', '45 Км Остановочный Пункт', 
     'Щербановка', 'Триполье-Днепровское', 'Стугна', 'Таценки', 'Новые Безрадичи', 'Марьяновская', 'Романков', 'Подгорцы', 'Лесники', 'Петр Кривонос', 'Проспект Науки', 
     'Выдубичи-Трипольские', 'Киев-Демеевский', 'Протасов Яр', 'Киев-Пасс.']

data = ['mironovka', 'pustovity', 'galino', 'kagarlyk', '71-km-ostanovochnyj-punkt,kievskaya-obl', 'rasava', 'lozy', 'zirki', 'ozernyj,kievskaya-obl', 'gordyn', 
 '45-km-ostanovochnyj-punkt,kievskaya-obl', 'shcherbanovka', 'tripole-dneprovskoe', 'stugna', 'tatsenki', 'novye-bezradichi', 'maryanovskaya', 'romankov', 
 'podgortsy', 'lesniki,kievskaya-obl', 'petr-krivonos', 'prospekt-nauki', 'vydubichi-tripolskie', 'kiev-demeevskij', 'protasov-yar', 'kiev-pass']


train_keyboard = InlineKeyboardMarkup(row_width=2)
for a,b in zip(title,data):
    train_keyboard.insert(InlineKeyboardButton(text=a, callback_data=b))



