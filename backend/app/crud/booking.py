from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.models.booking import Booking
from app.schemas.booking import BookingIn


def create_booking(booking: BookingIn, session: Session) -> Booking:
    db_booking = Booking(**booking.model_dump(), booked_at=datetime.utcnow())

    session.add(db_booking)
    session.commit()
    session.refresh(db_booking)

    return db_booking


def read_bookings(session: Session) -> List[Booking]:
    return session.query(Booking).filter_by(is_archived=False).all()


def read_booking(id: int, session: Session) -> Booking | None:
    return session.query(Booking).filter_by(id=id, is_archived=False).first()


def cancel_booking(id: int, session: Session) -> None:
    db_booking = session.query(Booking).filter_by(id=id, is_archived=False).first()

    db_booking.is_cancelled = True
    db_booking.cancelled_at = datetime.utcnow()

    session.commit()
