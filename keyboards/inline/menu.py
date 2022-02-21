from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='00:00', callback_data='00:00'),
            InlineKeyboardButton(text='01:00', callback_data='01:00'),
            InlineKeyboardButton(text='02:00', callback_data='02:00'),
            InlineKeyboardButton(text='03:00', callback_data='04:00'),

        ],
        [
            InlineKeyboardButton(text='04:00', callback_data='04:00'),
            InlineKeyboardButton(text='05:00', callback_data='05:00'),
            InlineKeyboardButton(text='06:00', callback_data='06:00'),
            InlineKeyboardButton(text='07:00', callback_data='07:00'),

        ],
        [
            InlineKeyboardButton(text='08:00', callback_data='08:00'),
            InlineKeyboardButton(text='09:00', callback_data='09:00'),
            InlineKeyboardButton(text='10:00', callback_data='10:00'),
            InlineKeyboardButton(text='11:00', callback_data='11:00'),

        ],
        [
            InlineKeyboardButton(text='12:00', callback_data='12:00'),
            InlineKeyboardButton(text='13:00', callback_data='13:00'),
            InlineKeyboardButton(text='14:00', callback_data='14:00'),
            InlineKeyboardButton(text='15:00', callback_data='15:00'),

        ],
        [
            InlineKeyboardButton(text='16:00', callback_data='16:00'),
            InlineKeyboardButton(text='17:00', callback_data='17:00'),
            InlineKeyboardButton(text='18:00', callback_data='18:00'),
            InlineKeyboardButton(text='19:00', callback_data='19:00'),

        ],
        [
            InlineKeyboardButton(text='20:00', callback_data='20:00'),
            InlineKeyboardButton(text='21:00', callback_data='21:00'),
            InlineKeyboardButton(text='22:00', callback_data='22:00'),
            InlineKeyboardButton(text='23:00', callback_data='23:00'),

        ],
        [
            InlineKeyboardButton(text='я спать 💤', callback_data='sleep'),
            InlineKeyboardButton(text='не работаю⛔️', callback_data='notwork'),
            InlineKeyboardButton(text='в отпуске 🏝', callback_data='weekend'),
        ]
    ]
)

menu2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад 🏝', callback_data='cancel'),
        ]
    ]
)

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Массовая рассылка 🏝', callback_data='mass_send'),
            InlineKeyboardButton(text='Отправить всем приветствие 🏝', callback_data='mass_start'),
        ]
    ]
)

user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Я на связи💚', callback_data='already'),
        ]
    ]
)