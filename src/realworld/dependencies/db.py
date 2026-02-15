from typing import AsyncGenerator

import asyncpg

from realworld.core.db import db


async def get_db_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    if not db.pool:
        raise RuntimeError("Database pool not initialized")

    async with db.pool.acquire() as connection:
        yield connection
