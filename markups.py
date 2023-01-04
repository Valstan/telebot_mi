from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnUpdate = KeyboardButton(text="Разбудить Афоню")
btnMapMalm = KeyboardButton(text="КАРТА Малмыжа")
btnDKmalmFhoto = KeyboardButton(text="ДК Малмыжа")
btnAfisha = KeyboardButton(text="АФИША Малмыжа")
btnStatMalm = KeyboardButton(text="Статистика МалмыжИнфо")
btnWeather = KeyboardButton(text="ПОГОДА")
btnBack = KeyboardButton(text="НАЗАД")
btnEsc = KeyboardButton(text="ВЫХОД")
btnCancel = KeyboardButton(text="ОТМЕНА")

kbMain = [
    [btnUpdate, btnAfisha, btnWeather],
    [btnMapMalm, btnDKmalmFhoto, btnStatMalm]
]

kbMainMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kbMain)

# Погодная Клавиатура -------------

btnWoblKirov = KeyboardButton(text="Кировская")
btnWoblTatar = KeyboardButton(text="Татарстан")
btnWoblUdmurt = KeyboardButton(text="Удмуртия")
btnWoblMariel = KeyboardButton(text="Мари Эл")

kbWobl = [
    [btnWoblKirov, btnWoblTatar],
    [btnWoblUdmurt, btnWoblMariel],
    [btnCancel]
]
kbWoblMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kbWobl)

btnWmalmig = KeyboardButton(text="Малмыж")
btnWkalinino = KeyboardButton(text="Калинино")
btnWsavali = KeyboardButton(text="Савали")
btnWrogki = KeyboardButton(text="Рожки")
btnWgonba = KeyboardButton(text="Гоньба")
btnWvpolyan = KeyboardButton(text="Вятские Поляны")


kbWcity = [
    [btnWmalmig, btnWkalinino, btnWsavali],
    [btnWrogki, btnWgonba, btnWvpolyan],
    [btnCancel]
]

kbWcityMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kbWcity)
