from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from realworld.core.db import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    app.state.db_pool = db.pool
    yield
    await db.disconnect()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World"}
