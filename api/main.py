# FastApi
from fastapi import FastAPI

# Local Imports
from routers.dog import router as dog_router
from routers.user import router as user_router


app =  FastAPI()

app.include_router(dog_router)
app.include_router(user_router)
