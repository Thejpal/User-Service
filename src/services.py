import jwt, uuid
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from src.db import User, session
from src.settings import settings
from src.model import UserModel
from passlib.hash import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login")

class UserService:
    def __init__(self):
        "Initializes the User service class"
        pass

    def __create_access_token(self, user: UserModel, expires_delta: timedelta = timedelta(minutes = 1)):
        "Creates a JWT token for the user"
        user_json = user.model_dump().copy()

        user_json.update({"exp" : datetime.now() + expires_delta})
        token = jwt.encode(payload = user_json, key = settings.jwt_secret_key, algorithm = settings.algorithm)
        return token

    def create_user(self, name: str, email: Optional[str], password: str) -> UserModel:
        "Registers a new user"
        if session.query(User).where(User.name == name).first():
            raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE, detail = "User with this name already exists")
        
        password_hash = bcrypt.hash(password)
        new_user = User(id = str(uuid.uuid4().int), name = name, email = email, password = password_hash)
        session.add(new_user)
        session.commit()
        
        registered_user = session.query(User).where(User.name == name).first()

        if not registered_user:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = "Failed to register the user")
        
        return UserModel(**registered_user.__dict__)
    
    def validate_user(self, user_name: str, password: str) -> str:
        "Validate user credentials"
        user = session.query(User).where(User.name == user_name and User.password == bcrypt.hash(password)).first()

        if user:
            return self.__create_access_token(user = UserModel(**user.__dict__))
        
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Invalid username or password")
    
def get_user(token: str = Depends(oauth2_scheme)):
    user_claims: dict = jwt.decode(jwt = token, key = settings.jwt_secret_key, algorithms = [settings.algorithm])

    if user_claims.get("user_id"):
        user = session.query(User).where(User.id == user_claims["user_id"]).first()

        if user:
            return UserModel(**user.__dict__)
        else:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid credentials")