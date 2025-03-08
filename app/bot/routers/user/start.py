from __future__ import annotations
from typing import TYPE_CHECKING

from logging import getLogger

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext

from database.session import new_session
from database.repository import UserRepository

from common.states import TestState

from .keyboards import ReplyMarkup

if TYPE_CHECKING: 
    from locales.types import I18nContext
    from sqlalchemy.ext.asyncio import AsyncSession


router = Router(name=__name__)
logger = getLogger(name=__name__)


@router.message(CommandStart())
async def _(
    message: Message, 
    i18n: I18nContext,
    db_session: AsyncSession,
    state : FSMContext
):
    user_repo = UserRepository(db_session)

    if (user:=await user_repo.get(chat_id=message.chat.id)):
        user = await user_repo.create(chat_id=message.chat.id)
        logger.info(f"Created new {user}")

    await message.answer(
        text=i18n.user.start(fullname=message.from_user.full_name),
        reply_markup=ReplyMarkup.get_start(i18n=i18n)
    )

    await state.set_state(TestState.start)


@router.message(TestState.start)
async def _(message : Message):
    await message.answer("Hello")



    
