from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.inspection import inspect
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
class Lead(BaseModel):
   __tablename__ = 'leads'
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, nullable=False)
   email = Column(String, nullable=False, index=True)
   postal_code = Column(String, index=True)
   status = Column(String, default='new')
   risk_score = Column(Integer, default=0)
   created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
