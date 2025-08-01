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
    session.commit()
    session.refresh(db_seats)

    return db_seats


def read_booked_seats(showtime_id: int, session: Session) -> List[Seat]:
    return session.query(Seat).filter_by(showtime_id=showtime_id, is_booked=True).all()
