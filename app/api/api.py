from fastapi import APIRouter

from api.routers import dog, user

api_router = APIRouter()
api_router.include_router(dog.router)
api_router.include_router(user.router)
