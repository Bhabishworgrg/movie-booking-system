from pydantic import BaseModel

class SeatOut(BaseModel):
    id: int
    number: str
