from pydantic import BaseModel

class SeatOut(BaseModel):
    id: int
    number: str
    is_booked: bool
