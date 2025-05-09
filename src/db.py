from sqlalchemy import String, Column, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.settings import settings

engine = create_engine(settings.database_url)
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = Column(String, nullable = False, unique = True)
    email = Column(String)
    password = Column(String, nullable = False)

# Base.metadata.create_all(engine)
Session = sessionmaker(engine)

session = Session()