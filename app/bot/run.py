import asyncio, logging, sys
<<<<<<< HEAD
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore

from routers import get_routers
from common.middleware.i18n import ContextManager
from utils.settings import get_telegram_settings


async def main():
    telegram_settings = get_telegram_settings()

    dp = Dispatcher()
    dp.include_routers(*get_routers())

    # * Middleware
    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="locales"),
        default_locale=telegram_settings.default_language,
        manager=ContextManager(),
    )

    # * Middleware Setup
    i18n_middleware.setup(dp)
=======

from redis.asyncio import Redis

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage

from routers import get_routers
from database.session import new_session
from common.middleware import setup_database_middleware, setup_i18n_middleware
from utils.settings import get_telegram_settings, get_redis_settings


async def main():

    # * Setup settings
    redis_settings = get_redis_settings()
    telegram_settings = get_telegram_settings()

    # * Setup storages and database
    postges_storage = new_session()
    redis_storage = RedisStorage(Redis.from_url(redis_settings.url))
    
    # * Setup dispatcher
    dp = Dispatcher(storage=redis_storage)

    # * Include routers
    dp.include_routers(*get_routers())

    # * Middleware Setup
    setup_i18n_middleware(dp, telegram_settings.default_language)
    setup_database_middleware(dp, postges_storage)
>>>>>>> 01a728c (update: DDD)


    bot = Bot(
        token=telegram_settings.bot_token   ,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
<<<<<<< HEAD
    asyncio.run(main())

=======

    try:
        asyncio.run(main())

    except (KeyboardInterrupt, asyncio.CancelledError):
        sys.exit(0)
>>>>>>> 01a728c (update: DDD)
