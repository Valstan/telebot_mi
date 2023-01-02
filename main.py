import asyncio
import logging

from aiogram import Bot, Dispatcher, types, methods
from aiogram.methods import SendMediaGroup
from aiogram.types import InputMediaPhoto, InputMedia

import config as cfg
import markups as nav
from afisha_mongo_base import afisha_mongo_base
from afisha_vk_wall import afisha_vk_wall

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher()


@dp.message(lambda message: message.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(
        f"Приветствую тебя, {message.from_user.first_name} {message.from_user.last_name}!\n"
        f"Меня зовут, Афоня. Я - Робот-Друг подписчиков телеграм-канала \"Малмыж Инфо\".\n"
        f"Ты можешь отправлять мне личные объявления, статьи, пожелания администрации сайта."
        f"Я все это сразу передам админу и он тебе поможет. Разместит твое объявление в ленте МалмыжИнфо, или статью, "
        f"или просто ответит на твои вопросы.\n"
        f"Нажимай на кнопочки меню внизу и я мгновенно покажу нужную тебе информацию!",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


@dp.message(lambda message: message.text == nav.btnStatMalm.text)
async def mess(message: types.Message):
    await message.answer(
        f"Вот ссылка на статистику - https://tgstat.ru/channel/@malmyzh_info/stat",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


@dp.message(lambda message: message.text == nav.btnMapMalm.text)
async def mess(message: types.Message):
    await message.answer(
        f"Вот ссылка на карту Малмыжа - https://yandex.ru/maps/20025/malmyzh/?ll=50.684234%2C56.518437&z=15",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


@dp.message(lambda message: message.text == nav.btnUpdate.text)
async def mess(message: types.Message):
    await message.answer(
        f"Упс... А я задремал? Извиняюсь )))\n"
        f"Я уже готов исполнять твои желания. Объявление? Статью? "
        f"Пиши, добавляй картинки и видео. Все размещу в ленте МалмыжИнфо!\n"
        f"А можешь просто написать сообщение админу. Он ответит\n"
        f"Возможно он сейчас тоже спит... Но я его разбужу! )",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


@dp.message(lambda message: message.text == nav.btnDKmalmFhoto.text)
async def mess(message: types.Message):
    await message.answer(
        f"Вот ссылка на фотографии из ДК Малмыжа с концерта прошедшего в апреле 2007 года "
        f"- https://disk.yandex.ru/a/Xt6n9vXOnFSQaQ",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


# А Ф И Ш А - АФИША - А ф и ш а
@dp.message(lambda message: message.text == nav.btnAfisha.text)
async def mess(message: types.Message):
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
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


@dp.message()
async def mess(message: types.Message):
    await message.answer(
        f"Спасибо, {message.from_user.first_name}, я передам твое сообщение админу МалмыжИнфо.\n"
        f"Он его прочитает и обязательно ответит или разместит его в ленте канала.\n"
        f"Пиши еще, я буду ждать! )",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, f"{message}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
