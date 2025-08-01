from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app.core.db import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    duration = Column(Integer, nullable=False)
    is_archived = Column(Boolean, server_default=expression.false(), nullable=False)
    archived_at = Column(DateTime)

    showtimes = relationship('Showtime', back_populates='movie', cascade='all, delete')
