from aiogram.types import CallbackQuery

from keyboards.inline.menu import admin, menu1
from loader import dp
from utils.db_api.database import db_select


@dp.callback_query_handler(text_contains='mass_start')
async def MassSendStart(call: CallbackQuery):
    id_users = db_select()
    await call.message.answer("Готово, нажмите /start", reply_markup=admin)
    for row in id_users:
        user_id = row[0]
        text = """
                Доброе Утро @{}!☀️
            Зай 😻, сегодня со скольки⏱ ?
                """.format(call.from_user.username)
        await call.bot.send_message(chat_id=user_id, text='''{}'''.format(text), reply_markup=menu1)
