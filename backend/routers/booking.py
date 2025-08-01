from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import Annotated, List

from backend.dependencies import get_db
from backend.crud import booking as crud
from backend.schemas.common import ResponseModel
from backend.schemas.booking import BookingIn, BookingOut


router = APIRouter(prefix='/bookings', tags=['bookings'])

SessionDep = Annotated[Session, Depends(get_db)]


@router.post('/', response_model=ResponseModel[BookingOut], status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingIn, session: SessionDep):
    try:
        data = crud.create_booking(booking, session)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid input or duplicate entry.'
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while creating the booking.'
        )
   
    return ResponseModel(
        data=data,
        code=status.HTTP_201_CREATED,
        message=f'Booking #{data.id} created successfully'
    )


@router.get('/', response_model=ResponseModel[List[BookingOut]])
def read_bookings(session: SessionDep):
    try:
        data = crud.read_bookings(session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving bookings.'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message='Bookings retrieved successfully'
    )


@router.get('/{id}', response_model=ResponseModel[BookingOut])
def read_booking(id: int, session: SessionDep):
    try:
        data = crud.read_booking(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving the booking.'
        )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Booking #{id} not found'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Booking #{id} retrieved successfully'
    )


@router.patch('/{id}', response_model=ResponseModel[BookingOut])
def update_booking(id: int, booking: BookingIn, session: SessionDep):
    try:
        data = crud.update_booking(id, booking, session)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Invalid input or duplicate entry.'
        )
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Booking #{id} not found'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Booking #{id} updated successfully'
    )


@router.patch('/{id}', response_model=ResponseModel[None])
def cancel_booking(id: int, session: SessionDep):
    try:
        success = crud.cancel_booking(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while cancelling the booking.'
        )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Booking #{id} not found'
        )

    return ResponseModel(
        data=None,
        code=status.HTTP_200_OK,
        message=f'Booking #{id} cancelled successfully'
    )
