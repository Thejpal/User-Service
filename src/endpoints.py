from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from src.model import UserModel
from src.services import UserService, get_user

auth = APIRouter()

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
    user_id: str

class Token(BaseModel):
    access_token: str
    token_type: str

@auth.post("/register")
def register_user(user_request: UserRequest, user_service: UserService = Depends()):
    user = user_service.create_user(name = user_request.name, email = user_request.email, password = user_request.password)
    return f"Hi {user.name}. Your registration is successful. Please login to continue."

@auth.get("/user", response_model = UserResponse)
def get_current_user(current_user: UserResponse = Depends(get_user)):
    return current_user

@auth.post("/login", response_model = Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends()):
    token = user_service.validate_user(user_name = form_data.username, password = form_data.password)

    return {"access_token": token, "token_type": "Bearer"}