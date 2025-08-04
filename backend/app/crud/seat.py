from sqlalchemy.orm import Session
from typing import List

from app.models.seat import Seat


def create_seats(showtime_id: int, session: Session) -> List[Seat]:
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columns = range(1, 11)

    db_seats = [
        Seat(showtime_id=showtime_id, number=f'{row}{column}')
        for row in rows for column in columns
    ]

    session.add_all(db_seats)
    session.flush()

    return db_seats


def read_booked_seats(showtime_id: int, session: Session) -> List[Seat]:
    return session.query(Seat).filter_by(showtime_id=showtime_id, is_booked=True).all()

def read_seats_for_booking(booking, session: Session) -> List[Seat]:
    return session.query(Seat).filter(
        Seat.id.in_(booking.seat_ids), 
        Seat.is_booked == False
    ).all()
