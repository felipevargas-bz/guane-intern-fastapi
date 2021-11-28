# FastApi
from fastapi import FastAPI

# Local Imports
from routers.dog import router


app =  FastAPI()

app.include_router(router)
