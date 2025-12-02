import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:yourpassword@localhost:5432/lead_management')
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine, autocommit=False)
Base = declarative_base()
# dependency
def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()
