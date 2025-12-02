from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..utils.jwt import create_access_token
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post('/signup', response_model=schemas.Token)
def signup(payload: schemas.UserCreate, db: Session = Depends(get_db)):
   user = db.query(models.User).filter(models.User.email ==
   payload.email).first()
   if user:
      raise HTTPException(status_code=400, detail='Email exists')
   hashed = pwd_context.hash(payload.password)
   user = models.User(email=payload.email, hashed_password=hashed)
   db.add(user); db.commit(); db.refresh(user)
   token = create_access_token(user.id)
   return {'access_token': token}

@router.post('/login', response_model=schemas.Token)
def login(payload: schemas.UserCreate, db: Session = Depends(get_db)):
   user = db.query(models.User).filter(models.User.email == payload.email).first()
   if not user or not pwd_context.verify(payload.password, user.hashed_password):
      raise HTTPException(status_code=400, detail='Invalid credentials')
   token = create_access_token(user.id)
   return {'access_token': token}

