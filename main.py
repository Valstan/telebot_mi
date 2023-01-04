import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import InputMediaPhoto

import config as cfg
import markups as nav
from afisha_mongo_base import afisha_mongo_base
from afisha_vk_wall import afisha_vk_wall
from get_stat_malm_info import get_stat_malm_info
from gismeteo import gismeteo
from message_filtre import message_filtre
from texts import text_updateKB, text_start

if cfg.mode == "develop":
    import logging

    logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher()


# ----------- СТАРТ --------- START ------------- Обновить клавиатуру, Нажми Меня, Выход, Отмена -----
@dp.message(lambda message:
            message.text in ("/start", "Обновить клавиатуру", "Нажми меня", nav.btnEsc.text, nav.btnCancel.text))
async def cmd_start(message: types.Message):
    if message.chat.type == "private":
        await message.answer(text_start(message), reply_markup=nav.kbMainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# Статистика Малмыж Инфо
@dp.message(lambda message: message.text == nav.btnStatMalm.text)
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"{get_stat_malm_info()}")
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# -------- Карта Малмыжа ----------
@dp.message(lambda message: message.text == nav.btnMapMalm.text)
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(
            f"Вот ссылка на карту Малмыжа - https://yandex.ru/maps/20025/malmyzh/?ll=50.684234%2C56.518437&z=15")
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# ----------- Обновить клавиатуру Разбудить Афоню -----------
@dp.message(lambda message: message.text == nav.btnUpdate.text)
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(text_updateKB(), reply_markup=nav.kbMainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# ----------- Фотографии ДК Малмыж -------------
@dp.message(lambda message: message.text == nav.btnDKmalmFhoto.text)
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(
            f"Вот ссылка на фотографии из ДК Малмыжа с концерта прошедшего в апреле 2007 года "
            f"- https://disk.yandex.ru/a/Xt6n9vXOnFSQaQ")
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# --------- А Ф И Ш А - АФИША - А ф и ш а ------------
@dp.message(lambda message: message.text == nav.btnAfisha.text)
async def mess(message: types.Message):
    if message.chat.type == "private":
        afisha_mongo = afisha_mongo_base()
        afisha_vk = afisha_vk_wall()
        media = []
        flag = True
        for foto in afisha_vk['attachments']:
            if flag:
                media.append(InputMediaPhoto(media=afisha_mongo[str(foto['photo']['id'])], caption=afisha_vk['text']))
                flag = False
            else:
                media.append(InputMediaPhoto(media=afisha_mongo[str(foto['photo']['id'])]))
        await bot.send_media_group(chat_id=message.chat.id, media=media)

    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# ----------- ПОГОДА ---------
@dp.message(lambda message: message.text in (nav.btnWeather.text, "погода", "Погода"))
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(
            f"{message.from_user.first_name}, выбери область, в которой находится город или село,"
            f" в котором ты хочешь узнать погоду:", reply_markup=nav.kbWoblMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# ----------- ПОГОДА ОБЛАСТЬ ---------
@dp.message(lambda message:
            message.text in (nav.btnWoblKirov.text, nav.btnWoblTatar.text, nav.btnWoblUdmurt.text, nav.btnWoblMariel.text))
async def mess(message: types.Message):
    if message.chat.type == "private":
        if message.text == "Кировская":
            await message.answer(
                f"{message.from_user.first_name}, ты выбрал Кировскую область."
                f" Теперь выбери населенный пункт на кнопках внизу, или набери название сам и отправь мне его.",
                reply_markup=nav.kbWcityMenu)
        else:
            await message.answer(
                f"{message.from_user.first_name}, ты выбрал регион - {message.text}."
                f" Теперь набери название населенного пункта и отправь мне его.")

            @dp.message()
            def pogoda_random(gorod: types.Message):
                if gorod.chat.type == "private":
                    gorod.answer(f"{gismeteo(f'{message.text} {gorod.text}')}", reply_markup=nav.kbWoblMenu)
                bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))

    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# ----------- ПОГОДА ГОРОД ---------
@dp.message(lambda message: message.text in
            (nav.btnWmalmig.text, nav.btnWkalinino.text, nav.btnWsavali.text,
             nav.btnWrogki.text, nav.btnWgonba.text, nav.btnWvpolyan.text))
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"{gismeteo(f'Кировская область {message.text}')}", reply_markup=nav.kbWcityMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# ПУСТОЕ ЗНАЧЕНИЕ РАНОДОМНЫЕ СТАТЬИ И ОБЪЯВЛЕНИЯ ----------
@dp.message()
async def mess(message: types.Message):
    if message.chat.type == "private":
        await message.answer(
            f"Спасибо, {message.from_user.first_name}, я передам твое сообщение админу МалмыжИнфо.\n"
            f"Он его прочитает и обязательно ответит или разместит его в ленте канала.\n"
            f"Пиши еще, я буду ждать! )",
            reply_markup=nav.kbMainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message_filtre(message))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
