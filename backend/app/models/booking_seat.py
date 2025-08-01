from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base

class BookingSeat(Base):
    __tablename__ = 'booking_seats'

    booking_id = Column(Integer, ForeignKey('bookings.id'), primary_key=True)
    seat_id = Column(Integer, ForeignKey('seats.id'), primary_key=True)
