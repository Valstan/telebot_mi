from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnStat = KeyboardButton(text="Статистика МалмыжИнфо", url="https://tgstat.ru/channel/@malmyzh_info/stat")
btnMap = KeyboardButton(text="Карта Малмыжа", url="https://yandex.ru/maps/20025/malmyzh/?ll=50.684234%2C56.518437&z=15")
btnUpdate = KeyboardButton("Разбудить Афоню")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnStat, btnMap)
mainMenu.add(btnUpdate)
