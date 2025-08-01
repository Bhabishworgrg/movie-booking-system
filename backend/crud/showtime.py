from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from backend.models.showtime import Showtime
from backend.schemas.showtime import ShowtimeIn, ShowtimeOut


def create_showtime(showtime: ShowtimeIn, session: Session) -> Showtime:
    db_showtime = Showtime(**showtime.model_dump()) 

    session.add(db_showtime)
    session.commit()
    session.refresh(db_showtime)

    return db_showtime


def read_showtimes(session: Session) -> List[Showtime]:
    return session.query(Showtime).filter_by(is_archived=False).all()


def read_showtime(id: int, session: Session) -> Showtime | None:
    return session.query(Showtime).filter_by(id=id, is_archived=False).first()


def update_showtime(id: int, showtime: ShowtimeIn, session: Session) -> Showtime | None:
    db_showtime = session.query(Showtime).filter_by(id=id, is_archived=False).first()

    if not db_showtime:
        return None
    
    for key, value in showtime.model_dump(exclude_unset=True).items():
        setattr(db_showtime, key, value)

    session.commit()
    session.refresh(db_showtime)

    return db_showtime


def archive_showtime(id: int, session: Session) -> bool:
    db_showtime = session.query(Showtime).filter_by(id=id, is_archived=False).first()
    
    if not db_showtime:
        return False 
    
    db_showtime.is_archived = True
    db_showtime.archived_at = datetime.utcnow()
    session.commit()

    return True
