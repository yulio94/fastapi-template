"""Base model"""

import typing
from datetime import datetime
from functools import reduce

from sqlalchemy import func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)


class Base(DeclarativeBase):
    id: typing.Any = None
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(
        onupdate=func.now(), nullable=True
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return reduce(
            lambda x, y: x + ("_" if y.isupper() else "") + y, cls.__name__
        ).lower()
