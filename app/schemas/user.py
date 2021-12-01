from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class CreateUser(UserBase):
    pass


class UpdateUser(BaseModel):
    name: Optional[str]
    username: Optional[str]
    password: Optional[str]


class SearchUser(BaseModel):
    name__icontains: Optional[str] = Field(None, alias="name")
    username__icontains: Optional[str] = Field(None, alias="username")


class UserInDB(UserBase):
    id: int
    created_at: datetime


class User(UserInDB):
    class Config:
        orm_mode = True

