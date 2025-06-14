from sqlalchemy import String, Column, create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError

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
        
    except OperationalError as e:
        logger.error(f"Database is not ready to accept connections yet. Waiting for it to get ready: {e}")

Session = sessionmaker(engine)
session = Session()