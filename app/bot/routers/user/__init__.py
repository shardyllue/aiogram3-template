from . import (
    start, 
    help
)


def get_routers():
    return [
        start.router,
        help.router
    ]



