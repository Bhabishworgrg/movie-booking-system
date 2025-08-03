from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.core.security import decode_jwt_token
from app.crud.auth import read_user_by_email
from app.models.user import User, Role


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DBSession = Annotated[Session, Depends(get_db)]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/v1/auth/login')

def get_current_user(session: DBSession, token: str = Depends(oauth2_scheme)) -> User:
    decoded_token = decode_jwt_token(token)
    if not decoded_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid access token'
        )

    email = decoded_token.get('email')
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid access token'
        )

    user = read_user_by_email(email, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid access token'
        )

    return user

CurrentUser = Annotated[User, Depends(get_current_user)]


def require_admin(user: CurrentUser) -> None:
    if user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Admin privileges required'
        )
