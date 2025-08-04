from sqlalchemy import Column, Integer, String, Text, Enum
from sqlalchemy.orm import relationship
import enum

from app.core.db import Base

class Role(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(Enum(Role), default=Role.USER, nullable=False)

    bookings = relationship('Booking', back_populates='user')
