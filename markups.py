from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnUpdate = KeyboardButton(text="Разбудить Афоню")
btnMapMalm = KeyboardButton(text="Карта Малмыжа")
btnDKmalmFhoto = KeyboardButton(text="ДК Малмыжа")
btnAfisha = KeyboardButton(text="АФИША Малмыжа")
btnStatMalm = KeyboardButton(text="Статистика МалмыжИнфо")


kb = [
    [btnUpdate, btnMapMalm, btnDKmalmFhoto],
    [btnAfisha, btnStatMalm]
]

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
