import os
from datetime import datetime, timedelta
from jose import jwt
SECRET = os.getenv('JWT_SECRET', 'supersecret')
ALGORITHM = 'HS256'
def create_access_token(subject: str, expires_delta: int = 60*60*2):
   expire = datetime.utcnow() + timedelta(seconds=expires_delta)
   to_encode = {'sub': str(subject), 'exp': expire}
   return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
def decode_token(token: str):
   return jwt.decode(token, SECRET, algorithms=[ALGORITHM])