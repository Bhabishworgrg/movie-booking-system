from pydantic import BaseModel
from datetime import datetime

class BookingIn(BaseModel):
    pass

class BookingOut(BookingIn):
    id: int
    booked_at: datetime
