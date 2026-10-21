# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base 


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'
# engine = create_engine(
#   SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
# )


# SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
# Base = declarative_base()

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Local fallback. Set DATABASE_URL in the deployment environment
# to use a configured, persistent database instead.
DEFAULT_DB_FILE = Path(__file__).resolve().parents[1] / "todos.db"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{DEFAULT_DB_FILE.as_posix()}",
)

connect_args = (
    {"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite:")
    else {}
)

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

