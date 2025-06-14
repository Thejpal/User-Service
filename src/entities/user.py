from sqlalchemy import String, Column

from src.database.db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key = True)
    name = Column(String, nullable = False, unique = True)
    email = Column(String)
    password = Column(String, nullable = False)