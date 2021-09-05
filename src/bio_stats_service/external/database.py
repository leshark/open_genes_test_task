from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..settings import settings


def get_db_url():
    user = settings.MYSQL_USER
    password = settings.MYSQL_PASSWORD
    server = settings.MYSQL_SERVER
    db = settings.MYSQL_DB
    return f"mysql+pymysql://{user}:{password}@{server}/{db}"


SQLALCHEMY_DATABASE_URL = get_db_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
