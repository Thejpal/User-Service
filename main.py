from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.auth.controller import auth
from src.middleware import CustomMiddleware
from src.logger import logger
from src.database.db import initialize_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting User Service....")

    initialize_database()
    
    yield
    logger.info("Stopping User Service....")

app = FastAPI(lifespan = lifespan)
app.add_middleware(middleware_class = CustomMiddleware)

app.router.include_router(router = auth, prefix = "/auth", tags = ["auth"])