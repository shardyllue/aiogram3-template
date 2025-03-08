from typing import TYPE_CHECKING
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram_i18n import I18nContext
if TYPE_CHECKING:
    from locales.types import I18nContext


def get_start(i18n : I18nContext):
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
        [KeyboardButton(text=i18n.user_reply_button.help())]
    ])


