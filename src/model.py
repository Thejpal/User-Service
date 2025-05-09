from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    user_id: UUID = Field(..., alias = "id")
    name: str
    email: Optional[str]