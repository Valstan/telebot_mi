import config as cfg
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Приветствую Вас, {message.from_user.first_name} {message.from_user.last_name}!\n"
        f"Я - Робот техподдержки подписчиков телеграм-канала \"Малмыж Инфо\".\n"
        f"Я пока не придумал себе имя и ничего не умею делать, кроме эха ваших слов.\n"
        f"Я в разработке :). Но скоро поумнею и буду помогать Вам!")


@dp.message_handler()
async def mess(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
