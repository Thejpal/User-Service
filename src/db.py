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

def initialize_database():
    i = 0
    while i<3:
        try:
            if not database_exists(engine.url):
                create_database(engine.url) # For creating postgresql database
                logger.info("Database created successfully")
            else:
                logger.debug("Database already exists")
            
            inspector = inspect(engine)
            if not inspector.has_table("user"):
                Base.metadata.create_all(engine) # For creating tables
                logger.info("User table created successfully")
            else:
                logger.debug("User table already exists")
            
            logger.debug("Breaking out of the loop after successful creation")
            break
        
        except Exception as e:
            i += 1
            time.sleep(2)
            logger.error(f"Failed to create database or table with error: {e}. Retrying times {i+1} after 2 seconds...")

Session = sessionmaker(engine)
session = Session()