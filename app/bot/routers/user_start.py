from logging import getLogger
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext
if TYPE_CHECKING: from locales.types import I18nContext

from common.keyboard import ReplyMarkup
from database.service import UserService


router = Router(name=__name__)
logger = getLogger(name=__name__)


@router.message(CommandStart())
async def on_start(
    message : Message, 
    state : FSMContext, 
    i18n : I18nContext
):
    if not await UserService.get(chat_id=message.chat.id):
        await UserService.create(chat_id=message.chat.id)

    await message.answer(
        text=i18n.user_text.start(username=message.from_user.first_name),
        reply_markup=ReplyMarkup.get_start_keyboard(i18n)
    )
    
    await state.clear()