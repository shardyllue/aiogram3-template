from functools import lru_cache
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from utils.settings import get_database_settings


@lru_cache(1)
def create_engine():
    settings = get_database_settings()

    return create_async_engine(url=settings.async_url)


def new_session():
    engine = create_engine()

    return async_sessionmaker(
        bind=engine, 
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
    )