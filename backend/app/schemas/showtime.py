from pydantic import BaseModel

class ShowtimeIn(BaseModel):
    start_time: str

class ShowtimeOut(ShowtimeIn):
    id: int
