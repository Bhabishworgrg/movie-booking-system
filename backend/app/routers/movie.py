from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import Annotated, List

from app.dependencies import get_db
from app.crud import movie as crud
from app.schemas.common import ResponseModel
from app.schemas.movie import MovieIn, MovieOut


router = APIRouter(prefix='/movies', tags=['movies'])

SessionDep = Annotated[Session, Depends(get_db)]


@router.post('/', response_model=ResponseModel[MovieOut], status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieIn, session: SessionDep):
    try:
        data = crud.create_movie(movie, session)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid input or duplicate entry.'
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while creating the movie.'
        )
   
    return ResponseModel(
        data=data,
        code=status.HTTP_201_CREATED,
        message=f'Movie #{data.id} created successfully'
    )


@router.get('/', response_model=ResponseModel[List[MovieOut]])
def read_movies(session: SessionDep):
    try:
        data = crud.read_movies(session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving movies.'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message='Movies retrieved successfully'
    )


@router.get('/{id}', response_model=ResponseModel[MovieOut])
def read_movie(id: int, session: SessionDep):
    try:
        data = crud.read_movie(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving the movie.'
        )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Movie #{id} not found'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Movie #{id} retrieved successfully'
    )


@router.patch('/{id}', response_model=ResponseModel[MovieOut])
def update_movie(id: int, movie: MovieIn, session: SessionDep):
    try:
        data = crud.update_movie(id, movie, session)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid input or duplicate entry.'
        )
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Movie #{id} not found'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Movie #{id} updated successfully'
    )


@router.patch('/{id}/archive', response_model=ResponseModel[None])
def archive_movie(id: int, session: SessionDep):
    try:
        success = crud.archive_movie(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while archiving the movie.'
        )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Movie #{id} not found'
        )

    return ResponseModel(
        data=None,
        code=status.HTTP_200_OK,
        message=f'Movie #{id} archived successfully'
    )
