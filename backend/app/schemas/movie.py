from pydantic import BaseModel

class MovieIn(BaseModel):
    name: str
    description: str
    duration: int

class MovieOut(MovieIn):
    id: int
