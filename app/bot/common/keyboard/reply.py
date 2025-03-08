from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram_i18n import I18nContext

def get_start_keyboard(i18n : I18nContext) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=i18n.user_reply_button.start())
            ]
        ],
        resize_keyboard=True
    )