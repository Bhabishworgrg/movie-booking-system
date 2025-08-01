from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import expression

from backend.core.db import Base

class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(4), nullable=False)
    is_booked = Column(Boolean, server_default=expression.false(), nullable=False)
