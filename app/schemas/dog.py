from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.schemas.user import UserInDB


class DogBase(BaseModel):
    name: str
    picture: str
    is_adopted: bool
    create_date: datetime
    update_date: datetime


class CreateDog(DogBase):
    id_user: Optional[int]


class UpdateDog(BaseModel):
    name: Optional[str]
    picture: Optional[str]
    is_adopted: Optional[str]


class SearchDog(BaseModel):
    id: Optional[int] = Field(None, alias="id")


class DogInDB(DogBase):
    id: int
    create_date: datetime

class Dog(UserInDB):
    class Config:
        orm_mode = True
