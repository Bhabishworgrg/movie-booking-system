from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import Annotated, List

from app.core.dependencies import DBSession, require_admin
from app.crud import showtime as crud
from app.schemas.common import ResponseModel
from app.schemas.showtime import ShowtimeIn, ShowtimeOut


router = APIRouter(prefix='/showtimes', tags=['showtimes'])


@router.post(
    '/', 
    response_model=ResponseModel[ShowtimeOut], 
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)]
)
def create_showtime(showtime: ShowtimeIn, session: DBSession):
    try:
        data = crud.create_showtime(showtime, session)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid input or duplicate entry.'
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while creating the showtime.'
        )
   
    return ResponseModel(
        data=data,
        code=status.HTTP_201_CREATED,
        message=f'Showtime #{data.id} created successfully'
    )


@router.get('/', response_model=ResponseModel[List[ShowtimeOut]])
def read_showtimes(session: DBSession):
    try:
        data = crud.read_showtimes(session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving showtimes.'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message='Showtimes retrieved successfully'
    )


@router.get('/{id}', response_model=ResponseModel[ShowtimeOut])
def read_showtime(id: int, session: DBSession):
    try:
        data = crud.read_showtime(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving the showtime.'
        )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Showtime #{id} not found'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Showtime #{id} retrieved successfully'
    )


@router.patch(
    '/{id}', 
    response_model=ResponseModel[ShowtimeOut],
    dependencies=[Depends(require_admin)]
)
def update_showtime(id: int, showtime: ShowtimeIn, session: DBSession):
    try:
        data = crud.update_showtime(id, showtime, session)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid input or duplicate entry.'
        )
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Showtime #{id} not found'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Showtime #{id} updated successfully'
    )


@router.patch(
    '/{id}/archive', 
    response_model=ResponseModel[None],
    dependencies=[Depends(require_admin)]
)
def archive_showtime(id: int, session: DBSession):
    try:
        success = crud.archive_showtime(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while archiving the showtime.'
        )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Showtime #{id} not found'
        )

    return ResponseModel(
        data=None,
        code=status.HTTP_200_OK,
        message=f'Showtime #{id} archived successfully'
    )
