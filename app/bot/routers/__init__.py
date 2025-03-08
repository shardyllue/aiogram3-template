from aiogram import Router

from . import (
<<<<<<< HEAD
    user_start,
    user_menu
=======
    user
>>>>>>> 01a728c (update: DDD)
)


def get_routers() -> list[Router]:
    return [
<<<<<<< HEAD
        user_start.router,
        user_menu.router
=======
        *user.get_routers(),
>>>>>>> 01a728c (update: DDD)
    ] 