from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, List

from app.core.dependencies import DBSession
from app.crud import seat as crud
from app.schemas.common import ResponseModel
from app.schemas.seat import SeatOut


router = APIRouter(tags=['showtimes'])


@router.get('/showtimes/{showtime_id}/booked-seats', response_model=ResponseModel[List[SeatOut]])
def read_booked_seats(showtime_id: int, session: DBSession):
    try:
        data = crud.read_booked_seats(showtime_id, session)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred while retrieving booked seats.'
        )

    return ResponseModel(
        data=data,
        code=status.HTTP_200_OK,
        message='Booked seats retrieved successfully'
    )
