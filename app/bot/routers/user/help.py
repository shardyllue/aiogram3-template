from __future__ import annotations
from typing import TYPE_CHECKING

from logging import getLogger
from aiogram import Router
from aiogram.types import Message

from aiogram_i18n import I18nContext
from aiogram_i18n.lazy import LazyFilter

if TYPE_CHECKING: 
    from locales.types import I18nContext


router = Router(name=__name__)
logger = getLogger(name=__name__)


@router.message(LazyFilter("user_reply_button-help"))
async def _(
    message: Message, 
    i18n: I18nContext,
):
    await message.answer(
        text=i18n.user.help()
    )



    
