from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.sql import expression

from backend.core.db import Base

class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, nullable=False, unique=True)
    is_archived = Column(Boolean, server_default=expression.false(), nullable=False)
    archived_at = Column(DateTime)
