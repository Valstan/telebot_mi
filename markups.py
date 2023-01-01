from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnStat = KeyboardButton(text="Статистика МалмыжИнфо")
btnMap = KeyboardButton(text="Карта Малмыжа")
btnDKmalm = KeyboardButton(text="ДК Малмыжа")
btnUpdate = KeyboardButton("Разбудить Афоню")
btnAfisha = KeyboardButton("АФИША Малмыжа")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnUpdate, btnMap, btnDKmalm)
mainMenu.add(btnStat)
