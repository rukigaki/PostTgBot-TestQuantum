from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings



engine = create_async_engine(settings.database_url_asyncpg)

session = async_sessionmaker(engine)


async def get_db():
    async with session() as s:
        yield s

