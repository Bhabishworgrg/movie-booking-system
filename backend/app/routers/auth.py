from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, List

from app.core.dependencies import DBSession
from app.core.security import verify_password, create_jwt_token
from app.crud import auth as crud
from app.schemas.common import ResponseModel
from app.schemas.auth import LoginRequest, RegisterRequest


router = APIRouter(prefix='/auths', tags=['auths'])


@router.post('/register', response_model=ResponseModel[None], status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest, session: DBSession):
    user = crud.read_user_by_email(request.email, session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Email already registered'
        )

    try:
        data = crud.create_user(request, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_BAD_REQUEST,
            detail='An unexpected error occurred while registering the user.'
        )

    return ResponseModel(
        data=None,
        code=status.HTTP_201_CREATED,
        message='User registered successfully'
    )


@router.post('/login', response_model=ResponseModel[None])
def login(request: LoginRequest, session: DBSession):
    user = crud.read_user_by_email(request.email, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid email or password'
        )

    is_correct_password = verify_password(request.password, user.password_hash)
    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid email or password'
        )

    token = create_jwt_token({
        'sub': user.id, 
        'email': user.email, 
        'username': user.username
    })
    return ResponseModel(
        data={'token': token},
        code=status.HTTP_200_OK,
        message='Login successful'
    )
