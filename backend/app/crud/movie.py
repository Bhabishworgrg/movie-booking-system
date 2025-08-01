from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.models.movie import Movie
from app.schemas.movie import MovieIn


def create_movie(movie: MovieIn, session: Session) -> Movie:
    db_movie = Movie(**movie.model_dump()) 

    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)

    return db_movie


def read_movies(session: Session) -> List[Movie]:
    return session.query(Movie).filter_by(is_archived=False).all()


def read_movie(id: int, session: Session) -> Movie | None:
    return session.query(Movie).filter_by(id=id, is_archived=False).first()


def update_movie(id: int, movie: MovieIn, session: Session) -> Movie | None:
    db_movie = session.query(Movie).filter_by(id=id, is_archived=False).first()

    if not db_movie:
        return None
    
    for key, value in movie.model_dump(exclude_unset=True).items():
        setattr(db_movie, key, value)

    session.commit()
    session.refresh(db_movie)

    return db_movie


def archive_movie(id: int, session: Session) -> bool:
    db_movie = session.query(Movie).filter_by(id=id, is_archived=False).first()
    
    if not db_movie:
        return False 
    
    db_movie.is_archived = True
    db_movie.archived_at = datetime.utcnow()
    session.commit()

    return True
