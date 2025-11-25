from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/lead_management"
engine=create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal=sessionmaker(bind=engine, autoflush=True, autocommit=False)