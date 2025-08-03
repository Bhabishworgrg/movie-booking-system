from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.core.security import hash_password


def create_user(request: RegisterRequest, session: Session) -> User:
    password_hash = hash_password(request.password)
    db_user = User(
        username=request.username,
        email=request.email,
        password_hash=password_hash
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def read_user_by_email(email: str, session: Session) -> User | None:
    return session.query(User).filter_by(email=email).first()
