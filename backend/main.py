from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Base, User
from db import engine, SessionLocal
from schemas import UserCreate, UserOut

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Users API")

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User
@app.post("/users_db", response_model=UserOut, status_code=201)
def create_user_db(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # FIX: use username not name
    user = User(username=payload.username, email=payload.email)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# List Users
@app.get("/users", response_model=List[UserOut])
def list_users(limit: int = 20, offset: int = 0, db: Session = Depends(get_db)):
    users = (
        db.query(User)
        .order_by(User.created_at.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )
    return users

