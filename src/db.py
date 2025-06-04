import time

from sqlalchemy import String, Column, create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy_utils import database_exists, create_database

from src.settings import settings
from src.logger import logger

engine = create_engine(settings.database_url)
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key = True)
    name = Column(String, nullable = False, unique = True)
    email = Column(String)
    password = Column(String, nullable = False)

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url) # For creating postgresql database
        logger.info("Database created successfully")
    else:
        logger.info("Database already exists")
    
    inspector = inspect(engine)
    if not inspector.has_table("user"):
        Base.metadata.create_all(engine) # For creating tables
        logger.info("User table created successfully")
    else:
        logger.info("User table already exists")

Session = sessionmaker(engine)

session = Session()