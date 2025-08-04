from pydantic import BaseModel
from datetime import datetime
from typing import List

from .showtime import ShowtimeOut
from .seat import SeatOut

class BookingIn(BaseModel):
    showtime_id: int
    seat_ids: List[int]

class BookingOut(BaseModel):
    id: int
    booked_at: datetime
    showtime: ShowtimeOut
    seats: List[SeatOut]
