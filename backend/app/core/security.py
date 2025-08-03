from passlib.context import CryptContext
from datetime import datetime
from jwt import encode, decode

from app.core.config import settings

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)

def create_jwt_token(data: dict) -> str:
    expire = datetime.utcnow() + settings.EXPIRES_DELTA
    to_encode = {**data, 'exp': expire}
     
    return encode(
        payload=to_encode,
        key=settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )

def decode_jwt_token(token: str) -> dict | None:
    try:
        return decode(
            jwt=token, 
            key=settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
    except:
        return None
