import logging
from typing import Any, Awaitable, Callable, Dict


from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Message, CallbackQuery



class LoggerMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.logger = logging.getLogger("aiogram-event")

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        
        if isinstance(event, Message):
            logging.info(f"Message: chat_id={event.chat.id} user_id={event.from_user.id} full_name={event.from_user.full_name} username={event.from_user.username}")

def setup_logger_middleware(dp : Dispatcher):
    _ = LoggerMiddleware()

    dp.message.middleware(_)
    dp.callback_query.middleware(_)