import asyncpg

from realworld.core.config import settings


class Database:
    def __init__(self):
        self.pool: asyncpg.Pool | None = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            dsn=str(settings.database_url),
            min_size=1,
            max_size=20,
        )

    async def disconnect(self):
        if self.pool:
            await self.pool.close()


db = Database()
