from aiogram.types import CallbackQuery
from keyboards.inline.menu import menu2, menu1
from loader import dp


@dp.callback_query_handler(text_contains='00:00')
async def time01(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 00:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='01:00')
async def time02(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 01:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='02:00')
async def time3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 02:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='03:00')
async def time4(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 03:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='04:00')
async def time5(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 04:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='05:00')
async def time6(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 05:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='06:00')
async def time7(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 06:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='07:00')
async def time8(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 07:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='08:00')
async def time9(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈")
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 08:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='09:00')
async def time10(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 09:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='10:00')
async def time11(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 10:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='11:00')
async def time12(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 11:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='12:00')
async def time13(call: CallbackQuery):
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 12:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='13:00')
async def time14(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 13:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='14:00')
async def time15(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 14:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='15:00')
async def time16(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 15:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='16:00')
async def time17(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 16:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='17:00')
async def time18(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 17:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='18:00')
async def time19(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 18:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='19:00')
async def time20(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 19:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='20:00')
async def time21(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 20:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='21:00')
async def time22(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 21:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='22:00')
async def time23(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 22:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='23:00')
async def time24(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Спасибо за ответ , хорошего настроение 🤗 и позитивного дня🌈", reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
🧏🏻‍♀️Девушка с псевдонимом: @{}
⏰Вышла на работу в 23:00'''.format(call.from_user.username), reply_markup=menu2)


@dp.callback_query_handler(text_contains='sleep')
async def sleep(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = """
        Сладких снов, {}!☀️
    Добрых снов 🤗 и мягкой кроватки 🌈
        """.format(call.message.from_user.full_name)
    await call.message.edit_text(text, reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
    🧏🏻‍♀️Девушка с псевдонимом: @{}
    ⏰Отправилась спать, пожелаем ей сладких снов'''.format(call.from_user.username))


@dp.callback_query_handler(text_contains='notwork')
async def notwork(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = """
        Хорошо отдохнуть, {}!☀️
    Продуктивного дня 🤗 и решения всех незаконченых дел! 🌈
        """.format(call.message.from_user.full_name)
    await call.message.edit_text(text, reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
    🧏🏻‍♀️Девушка с псевдонимом: @{}
    ⏰Сегодня не будет работать, пожелаем ех хорошо отдохнуть!'''.format(call.from_user.username))


@dp.callback_query_handler(text_contains='weekend')
async def weekend(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = """
        Хорошо отдохнуть, {}!☀️
    Продуктивного отпуска 🤗 и отрывного веселия! 🌈
        """.format(call.message.from_user.full_name)
    await call.message.edit_text(text, reply_markup=menu2)
    await call.message.bot.send_message(chat_id=934718523, text='''
    🧏🏻‍♀️Девушка с псевдонимом: @{}
    ⏰Отправилась в отпуск, пожелаем ей хорошо отдохнуть!'''.format(call.from_user.username))


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    text = """
        Доброе Утро {}!☀️
    Зай 😻, сегодня со скольки⏱ ?
        """.format(call.message.from_user.full_name)
    await call.message.edit_text(text, reply_markup=menu1)
