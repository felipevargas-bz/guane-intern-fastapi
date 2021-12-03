from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class DogBase(BaseModel):
    name: str
    picture: str
    is_adopted: bool
    id_user: int


class CreateDog(DogBase):
    pass


class UpdateDog(BaseModel):
    name: Optional[str]
    picture: Optional[str]
    is_adopted: Optional[str]
    id_user: Optional[int]


class SearchDog(BaseModel):
    name__icontains: Optional[str] = Field(None, alias="name")
    id__icontains: Optional[int] = Field(None, alias="id")


class DogInDB(DogBase):
    id: int
    create_date: datetime

class Dog(DogInDB):
    class Config:
        orm_mode = True
