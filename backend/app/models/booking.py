from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app.core.db import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    booked_at = Column(DateTime, nullable=False)
    cancelled_at = Column(DateTime)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)

    showtime = relationship('Showtime', back_populates='bookings')
    seats = relationship('Seat', secondary='booking_seats', back_populates='bookings')
