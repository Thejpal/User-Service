from fastapi import FastAPI
from src.endpoints import auth
from src.middleware import CustomMiddleware
from src.logger import logger

app = FastAPI()
app.add_middleware(middleware_class = CustomMiddleware)

logger.info("Starting User Service....")

app.router.include_router(router = auth, prefix = "/auth", tags = ["auth"])