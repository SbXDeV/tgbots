from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.menu import user
from loader import dp
# await call.message.bot.send_message(chat_id=1909188068, text='''{}''')
from states.mass import MassSend
from utils.informations import admin_id
from utils.db_api.database import db_select


@dp.callback_query_handler(text_contains='mass_send', state=None)
async def MassSendQ1(call: CallbackQuery):
    await call.message.edit_text("Введите сообщение для массовой рассылки")
    await MassSend.text.set()


@dp.message_handler(state=MassSend.text)
async def MassSendQ2(message: types.Message, state: FSMContext):
    answer = message.text
    id_users = db_select()
    await message.answer("Начинаю массовую рассылку вашего сообщения, пожалуйста подождите!")
    for row in id_users:
        user_id = row[0]
        if user_id == str(admin_id):
            pass
        else:
            await message.bot.send_message(chat_id=user_id, text='''{}'''.format(answer), reply_markup=user)
    await state.finish()


@dp.callback_query_handler(text_contains='already')
async def MassSendQ1(call: CallbackQuery):
    await call.message.answer("Спасибо, отправляю данные заказчику")
    await call.bot.send_message(chat_id=admin_id,
                                text='''Девушка с псевдонимом @{}, готова выполнить заказ!'''.format(call.from_user.username))