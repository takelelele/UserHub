from datetime import datetime, timezone

from sqlalchemy import BIGINT, func
from sqlalchemy.orm import mapped_column, Mapped

from database import Base


class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now()
    )
