from pydantic import BaseModel, ConfigDict
from typing import Generic, TypeVar

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    data: T | None
    code: int
    message: str

    model_config = ConfigDict(exclude_none=True)
