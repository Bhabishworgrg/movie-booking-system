from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app.core.db import Base

class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(4), nullable=False)
    is_booked = Column(Boolean, server_default=expression.false(), nullable=False)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)

    showtime = relationship('Showtime', back_populates='seats')
    bookings = relationship('Booking', secondary='booking_seats', back_populates='seats')
