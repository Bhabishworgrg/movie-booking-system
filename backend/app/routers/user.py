from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import DBSession, CurrentUser
from app.schemas.common import ResponseModel
from app.schemas.booking import BookingOut
from app.crud import booking
from app.models.user import Role


router = APIRouter(prefix='/users', tags=['users'])


@router.get('/{id}/bookings', response_model=ResponseModel[List[BookingOut]])
def read_bookings_by_user(id: int, session: DBSession, user: CurrentUser):
    if user.id != id and not user.role == Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have permission to view this user\'s bookings.'
        )

    try:
        data = booking.read_bookings_by_user(id, session)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving user bookings.' + str(e)
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message='User bookings retrieved successfully'
    )
