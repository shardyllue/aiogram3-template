<<<<<<< HEAD
=======
from aiogram import Dispatcher
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
>>>>>>> 01a728c (update: DDD)
from aiogram_i18n.managers import BaseManager
from aiogram.types import User


class ContextManager(BaseManager):
    
    async def get_locale(self, event_from_user : User) -> str:
        return event_from_user.language_code
    

<<<<<<< HEAD
    async def set_locale(self, Locale : str): ...
=======
    async def set_locale(self, Locale : str): ...



def setup_i18n_middleware(dp : Dispatcher, default_language : str):
    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="locales"),
        default_locale=default_language,
        manager=ContextManager(),
    )

    # * Middleware Setup
    i18n_middleware.setup(dp)
>>>>>>> 01a728c (update: DDD)
