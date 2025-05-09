from typing import Optional
from fastapi import HTTPException, status
from src.db import User, session
from src.model import UserModel
from passlib.hash import bcrypt

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