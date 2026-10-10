import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

db_password = os.getenv("db_password")
database = os.getenv("database")
db_user = os.getenv("db_user")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{db_user}:{db_password}@localhost:5432/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

