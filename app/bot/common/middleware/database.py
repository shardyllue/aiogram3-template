import inspect
from typing import Any, Awaitable, Callable, Dict

from sqlalchemy.ext.asyncio import async_sessionmaker

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Message, CallbackQuery



class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, sessionmaker : async_sessionmaker) -> None:
        self.Session = sessionmaker

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
                
        async with self.Session() as session:
            data["db_session"] = session
            
            try:
                return await handler(event, data)
            except Exception as e:
                await session.rollback()
                raise e

def setup_database_middleware(dp : Dispatcher, sessionmaker : async_sessionmaker):
    _ = DatabaseMiddleware(sessionmaker)

    dp.message.middleware(_)
    dp.callback_query.middleware(_)