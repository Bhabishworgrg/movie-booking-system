from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app.core.db import Base

class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, nullable=False, unique=True)
    is_archived = Column(Boolean, server_default=expression.false(), nullable=False)
    archived_at = Column(DateTime)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)

    movie = relationship('Movie', back_populates='showtimes')
    seats = relationship('Seat', back_populates='showtime', cascade='all, delete')
    bookings = relationship('Booking', back_populates='showtime', cascade='all, delete')
