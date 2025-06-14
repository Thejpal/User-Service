from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException, Request, Response
from fastapi.responses import JSONResponse

from src.logger import logger
from src.context import request_context

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            path = request.url.path
            method = request.method
            request_context.set({
                "request_id": str(uuid4()),
                "path": path,
                "method": method,
                "client_ip": request.client.host if request.client is not None else "None"
            })
            
            logger.info(f"Request: {method} {path}")
            response = await call_next(request)
            
            if "application/json" in response.headers.get("content-type", ""):
                response.headers["content-type"] = "application/json; charset=utf-8"

            return response
        
        except HTTPException as e:
            logger.error(f"Error processing request: {e.detail}")
            return JSONResponse(
                status_code = e.status_code,
                content = {"detail": e.detail},
                media_type = "application/json; charset=utf-8"
            )
        
        finally:
            request_context.set({})