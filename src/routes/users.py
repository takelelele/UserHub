from typing import List

from litestar import Router, get, post, patch, delete, status_codes
from litestar.di import Provide
from litestar.exceptions import HTTPException
from pydantic import TypeAdapter
from sqlalchemy import (
    select,
    update,
    delete as delete_q
)
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models.users import Users
from schema.users import CreateUserSchema, UserSchema, UpdateUserSchema


@post(
    path="/create",
    dependencies={
        "db": Provide(get_db),
    },
    tags=["Users"]
)
async def create_user(
        db: AsyncSession,
        data: CreateUserSchema
) -> UserSchema:
    user = Users(
        name=data.name,
        surname=data.surname,
        password=data.password
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserSchema.model_validate(user)


@get(
    path="/all",
    dependencies={
        "db": Provide(get_db),
    },
    tags=["Users"]
)
async def all_users(
        db: AsyncSession
) -> list[UserSchema]:
    users = await db.scalars(select(Users))

    return TypeAdapter(List[UserSchema]).validate_python(users)


@get(
    path="/{user_id: int}",
    dependencies={
        "db": Provide(get_db),
    },
    tags=["Users"]
)
async def user_by_id(
        user_id: int,
        db: AsyncSession
) -> UserSchema:
    user = await db.scalar(
        select(Users)
        .where(Users.id == user_id)
    )

    if user:
        return UserSchema.model_validate(user)

    raise HTTPException(
        status_code=status_codes.HTTP_404_NOT_FOUND,
        detail="Пользователя с таким user_id не существует"
    )


@patch(
    path="/update/{user_id: int}",
    dependencies={
        "db": Provide(get_db),
    },
    tags=["Users"]
)
async def update_user_data(
        user_id: int,
        db: AsyncSession,
        data: UpdateUserSchema
) -> UserSchema:
    user = await db.scalar(
        update(Users)
        .where(Users.id == user_id)
        .values(**data.model_dump(exclude_none=True))
        .returning(Users)
    )

    if user:
        await db.commit()
        await db.refresh(user)

        return UserSchema.model_validate(user)

    raise HTTPException(
        status_code=status_codes.HTTP_404_NOT_FOUND,
        detail="Пользователя с таким user_id не существует"
    )


@delete(
    path="/delete/{user_id: int}",
    dependencies={
        "db": Provide(get_db),
    },
    tags=["Users"]
)
async def delete_user(
        user_id: int,
        db: AsyncSession,
) -> None:
    user = await db.scalar(
        delete_q(Users)
        .where(Users.id == user_id)
        .returning(Users)
    )

    if user:
        await db.commit()

        return None

    raise HTTPException(
        status_code=status_codes.HTTP_404_NOT_FOUND,
        detail="Пользователя с таким user_id не существует"
    )


router = Router(
    path="/users",
    route_handlers=[create_user, all_users, user_by_id, update_user_data, delete_user]
)
