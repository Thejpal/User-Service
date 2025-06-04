from typing import Optional

from pydantic import BaseModel, Field

class UserModel(BaseModel):
    user_id: str = Field(..., alias = "id")
    name: str
    email: Optional[str]