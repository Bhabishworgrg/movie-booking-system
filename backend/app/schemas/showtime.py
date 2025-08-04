from pydantic import BaseModel
from datetime import datetime
from typing import List

from .movie import MovieOut
from .seat import SeatOut

class ShowtimeIn(BaseModel):
    start_time: datetime 
    movie_id: int

class ShowtimeOut(ShowtimeIn):
    id: int
    movie: MovieOut
    seats: List[SeatOut]
