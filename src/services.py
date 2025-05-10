from typing import Optional
import uuid
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from src.db import User, session
from src.model import UserModel
from passlib.hash import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login")

class UserService:
    def __init__(self):
        "Initializes the User service class"
        pass

    def create_user(self, name: str, email: Optional[str], password: str) -> UserModel:
        "Registers a new user"
        if session.query(User).where(User.name == name).first():
            raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE, detail = "User with this name already exists")
        
        password_hash = bcrypt.hash(password)
        new_user = User(name = name, email = email, password = password_hash)
        session.add(new_user)
        session.commit()
        
        registered_user = session.query(User).where(User.name == name).first()

        if not registered_user:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = "Failed to register the user")
        
        return UserModel(**registered_user.__dict__)
    
    def validate_user(self, user_name: str, password: str) -> UserModel:
        "Validate user credentials"
        user = session.query(User).where(User.name == user_name and User.password == bcrypt.hash(password)).first()

        if user:
            return UserModel(**user.__dict__)
        
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Invalid credentials")
    
def get_user(token: str = Depends(oauth2_scheme)):
    user = session.query(User).where(User.name == token).first()

    if user:
        return UserModel(**user.__dict__)
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, details = "User not found")