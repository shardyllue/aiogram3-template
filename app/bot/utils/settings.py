from logging import getLogger

from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache


logger = getLogger(name=__name__)


<<<<<<< HEAD
=======
class RedisSettings(BaseSettings):

    url : str = Field(validation_alias="REDIS_URL")

>>>>>>> 01a728c (update: DDD)
class DatabaseSettings(BaseSettings):
    
    sync_url: str = Field(validation_alias="DATABASE_SYNC_URL")
    async_url: str = Field(validation_alias="DATABASE_ASYNC_URL")


class TelegramSettings(BaseSettings):


    bot_token: str = Field(
        validation_alias="TELEGRAM_BOT_TOKEN"
    )
    
    default_language: str = Field(
        validation_alias="TELEGRAM_DEFAULT_LANGUAGE", 
        default="en"
    )

<<<<<<< HEAD

=======
@lru_cache(1)
>>>>>>> 01a728c (update: DDD)
def _load_enviroment() -> None:
    """Loading dotnev if it needed
    """
    from os import environ, path
    if not (_dotenv_path:=environ.get("DOTENV_PATH")): return 
    
    logger.debug("Loading development enviroment from .env.dev")
    from dotenv import load_dotenv

<<<<<<< HEAD
    load_dotenv(path.join(_dotenv_path, ".env.dev"))
=======
    load_dotenv(_dotenv_path)
>>>>>>> 01a728c (update: DDD)


@lru_cache(1)
def get_telegram_settings() -> TelegramSettings:
    _load_enviroment()
    
    return TelegramSettings()


@lru_cache(1)
def get_database_settings() -> DatabaseSettings:
    _load_enviroment()
    
<<<<<<< HEAD
    return DatabaseSettings()
=======
    return DatabaseSettings()


@lru_cache(1)
def get_redis_settings() -> RedisSettings:
    _load_enviroment()
    
    return RedisSettings()
>>>>>>> 01a728c (update: DDD)
