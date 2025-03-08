from __future__ import annotations
from typing import TYPE_CHECKING

from database.base import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository:

    def __init__(self, session : AsyncSession):
        self.session = session


    async def get(self, chat_id : int) -> User | None:
        return await self.session.get(User, chat_id)
        
        
    async def create(self, chat_id : int) -> User:
        user = User(chat_id=chat_id)

        self.session.add(user)
        await self.session.commit()

        return user