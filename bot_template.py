import config as cfg
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handlers(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет")


@dp.message_handlers()
async def mess(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
