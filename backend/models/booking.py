from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import expression

from backend.core.db import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    booked_at = Column(DateTime, nullable=False)
    cancelled_at = Column(DateTime)
