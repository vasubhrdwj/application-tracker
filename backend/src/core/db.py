from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from src.core.config import settings
from typing import Union, Any

DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True  # Enables SQLAlchemy 2.0 style usage
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True 
)

Base = declarative_base()

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

def get_db() -> Union[Session, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()