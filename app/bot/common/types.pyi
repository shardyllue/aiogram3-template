from contextlib import contextmanager
from typing import Any, Generator, Union

from aiogram_i18n import LazyProxy


class User_Reply_Button:
    def start(self) -> str: ...

class User_Text:
    def start(self, *, username: Any) -> str: ...
    def menu(self) -> str: ...

class I18nStubs:
    user_text = User_Text()
    user_reply_button = User_Reply_Button()

class I18nContext(I18nStubs):
    def get(self, key: str, /, **kwargs: Any) -> str: ...
    async def set_locale(self, locale: str, **kwargs: Any) -> None: ...
    @contextmanager
    def use_locale(self, locale: str) -> Generator[I18nContext, None, None]: ...
    @contextmanager
    def use_context(self, **kwargs: Any) -> Generator[I18nContext, None, None]: ...
    def set_context(self, **kwargs: Any) -> None: ...

class LazyFactory(I18nStubs):
    key_separator: str
    def set_separator(self, key_separator: str) -> None: ...
    def __call__(self, key: str, /, **kwargs: dict[str, Any]) -> LazyProxy: ...

L: LazyFactory
