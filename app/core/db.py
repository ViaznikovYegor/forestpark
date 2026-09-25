from collections.abc import AsyncGenerator

from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import (
    async_sessionmaker, AsyncSession, create_async_engine
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)
from app.core.config import settings


class Base(DeclarativeBase):
    pass


class CommonMixin:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True)


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as async_session:
        yield async_session
