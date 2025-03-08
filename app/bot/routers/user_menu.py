from logging import getLogger
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_i18n import LazyFilter
from aiogram_i18n import I18nContext
if TYPE_CHECKING: from locales.types import I18nContext


router = Router(name=__name__)
logger = getLogger(name=__name__)


@router.message(LazyFilter("user_reply_button-start"))
async def on_menu(
    message : Message, 
    state : FSMContext, 
    i18n : I18nContext
):

    await message.answer(
        text=i18n.user_text.menu(),
    )
    
    await state.clear()