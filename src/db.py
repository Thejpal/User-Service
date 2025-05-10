from sqlalchemy import String, Column, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from src.settings import settings

engine = create_engine(settings.database_url)
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key = True)
    name = Column(String, nullable = False, unique = True)
    email = Column(String)
    password = Column(String, nullable = False)

# Base.metadata.create_all(engine)
Session = sessionmaker(engine)

session = Session()