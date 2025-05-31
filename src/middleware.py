from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from src.logger import logger

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        path = request.url.path
        method = request.method
        
        logger.info(f"Request: {method} {path}")
        response = await call_next(request)
        
        if "application/json" in response.headers.get("content-type", ""):
            response.headers["content-type"] = "application/json; charset=utf-8"

        return response