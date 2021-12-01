from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api import api_router
from infra.mysql.config import (
    generate_schema,
    init_db,
)


def create_application():

    app = FastAPI()

    app.include_router(api_router, prefix="/api")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    init_db(app)
    await generate_schema()
