from logging import getLogger

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


log = getLogger(__name__)


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url='mysql://root:6232@mysql:3306/test_guane',
        modules={"models": ["infra.mysql.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(
        db_url='mysql://root:6232@mysql:3306/test_guane',
        modules={"models": ["infra.mysql.models"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
