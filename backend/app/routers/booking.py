from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import Annotated, List

from app.core.dependencies import DBSession, CurrentUser
from app.crud import booking as crud
from app.schemas.common import ResponseModel
from app.schemas.booking import BookingIn, BookingOut


router = APIRouter(prefix='/bookings', tags=['bookings'])


@router.post('/', response_model=ResponseModel[BookingOut], status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingIn, session: DBSession, user: CurrentUser):
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
def read_bookings(session: DBSession):
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
def read_booking(id: int, session: DBSession, user: CurrentUser):
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

    if data.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have permission to access this booking'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message=f'Booking #{id} retrieved successfully'
    )


@router.patch('/{id}/cancel', response_model=ResponseModel[None])
def cancel_booking(id: int, session: DBSession, user: CurrentUser):
    booking = crud.read_booking(id, session)

    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Booking #{id} not found'
        )

    if booking.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have permission to cancel this booking'
        )

    try:
        crud.cancel_booking(id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while cancelling the booking.'
        )

    return ResponseModel(
        data=None,
        code=status.HTTP_200_OK,
        message=f'Booking #{id} cancelled successfully'
    )
