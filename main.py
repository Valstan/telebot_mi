import config as cfg
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Text(equals="start"))
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Будь здоров, {message.from_user.first_name} {message.from_user.last_name}!\n"
        f"Меня зовут, Афоня. Я - Робот-Друг подписчиков телеграм-канала \"Малмыж Инфо\".\n"
        f"Ты можешь отправлять мне личные объявления, статьи, пожелания администрации сайта."
        f"Я все это сразу передам админу и он тебе поможет. Разместит твое объявление в ленте МалмыжИнфо, или статью, "
        f"или просто ответит на твои вопросы.\n"
        f"Нажимай на кнопочки меню внизу и я мгновенно покажу нужную тебе информацию!",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message)


@dp.message_handler(lambda message: message.text == nav.btnStat.text)
async def mess(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Вот ссылка на статистику - https://tgstat.ru/channel/@malmyzh_info/stat",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message)


@dp.message_handler(lambda message: message.text == nav.btnMap.text)
async def mess(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Вот ссылка на карту Малмыжа - https://yandex.ru/maps/20025/malmyzh/?ll=50.684234%2C56.518437&z=15",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message)


@dp.message_handler(lambda message: message.text == nav.btnUpdate.text)
async def mess(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Упс... А я задремал? Извиняюсь )))\n"
        f"Я уже готов исполнять твои желания. Объявление? Статью? "
        f"Пиши, добавляй картинки и видео. Все размещу в ленте МалмыжИнфо!\n"
        f"А можешь просто написать сообщение админу. Он ответит\n"
        f"Возможно он сейчас тоже спит... Но я его разбужу! )",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message)


@dp.message_handler()
async def mess(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Спасибо, {message.from_user.first_name}, я передам твое сообщение админу МалмыжИнфо.\n"
        f"Он его прочитает и обязательно ответит или разместит его в ленте канала.\n"
        f"Пиши еще, я буду ждать! )",
        reply_markup=nav.mainMenu)
    await bot.send_message(cfg.MAIN_USER_ID, message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
