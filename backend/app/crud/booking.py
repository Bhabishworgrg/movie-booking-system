from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.models.booking import Booking
from app.models.booking_seat import BookingSeat
from app.models.seat import Seat
from app.schemas.booking import BookingIn


def create_booking(booking: BookingIn, session: Session, user_id: int) -> Booking:
    db_booking = Booking(
        showtime_id=booking.showtime_id, 
        booked_at=datetime.utcnow(), 
        user_id=user_id
    )

    session.add(db_booking)
    session.flush()

    db_booking_seats = [
        BookingSeat(booking_id=db_booking.id, seat_id=seat_id)
        for seat_id in booking.seat_ids
    ]

    session.add_all(db_booking_seats)

    session.query(Seat).filter(Seat.id.in_(booking.seat_ids)).update(
        {Seat.is_booked: True}, 
        synchronize_session='fetch'
    )

    session.commit()

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
