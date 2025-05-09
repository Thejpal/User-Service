from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, model_validator
from src.model import UserModel
from src.services import UserService
from uuid import UUID

app = FastAPI()

class UserRequest(BaseModel):
    name: str
    email: Optional[str]
    password: str = Field(..., min_length = 5)
    confirm_password: str

    @model_validator(mode = "after")
    def validate_password(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords don't match. Please check and try again.")
        
        return self

class UserResponse(UserModel):
    user_id: UUID

@app.post("/auth/register", response_model = UserResponse)
def register_user(user_request: UserRequest, user_service: UserService = Depends()):
    user = user_service.create_user(name = user_request.name, email = user_request.email, password = user_request.password)
    return user