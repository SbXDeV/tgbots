from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import menu
from keyboards.inline.menu import admin
from loader import dp
from utils.db_api.database import db_insert


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id == 934718523:
        await message.answer('Добро пожаловать, это админ панель бота, функцоинал можно купить у @sbxdeveloper', reply_markup=admin)
    else:

        db_insert(message.from_user.id,
                  message.from_user.username,
                  message.from_user.first_name,
                  message.from_user.last_name)
        text = """
        Доброе Утро @{}!☀️
    Зай 😻, сегодня со скольки⏱ ?
        """.format(message.from_user.username)
        await message.answer(text, reply_markup=menu.menu1)
