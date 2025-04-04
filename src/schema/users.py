from pydantic import BaseModel, ConfigDict


class CreateUserSchema(BaseModel):
    name: str
    surname: str
    password: str


class UserSchema(BaseModel):
    id: int
    name: str
    surname: str

    model_config = ConfigDict(from_attributes=True)


class UpdateUserSchema(BaseModel):
    name: str = None
    surname: str = None
    password: str = None
