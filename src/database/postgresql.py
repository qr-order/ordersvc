from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import get_postgres_url

SQLALCHEMY_DATABASE_URL = get_postgres_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()
