from typing import Optional

from msgspec import Struct


class CreateUserSchema(Struct):
    name: str
    surname: str
    password: str


class UserSchema(Struct):
    id: int
    name: str
    surname: str


class UpdateUserSchema(Struct):
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None
