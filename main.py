from fastapi import FastAPI
from src.endpoints import auth
from middleware import CustomMiddleware
from logger import logger

app = FastAPI()
app.add_middleware(middleware_class = CustomMiddleware)

logger.info("Starting User Service....")

app.router.include_router(router = auth, prefix = "/auth", tags = ["auth"])