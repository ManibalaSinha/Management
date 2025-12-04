from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class LeadCreate(BaseModel):
   name: str
   email: EmailStr
   postal_code: Optional[str]

class LeadOut(BaseModel):
   id: int
   name: str
   email: EmailStr
   postal_code: Optional[str]
   status: str
   risk_score: int
   created_at: str
   class Config:
      orm_mode = True

class Token(BaseModel):
   access_token: str
   token_type: str = 'bearer'

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }