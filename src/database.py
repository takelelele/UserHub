from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from userhub import settings

engine = create_async_engine(settings.SQLALCHEMYURL)

Session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


async def get_db():
    async with Session() as session:
        yield session
