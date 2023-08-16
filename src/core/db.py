from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from src.config import settings


Base = declarative_base()

engine = create_engine(settings.db.url, future=True)


def get_session():
    session = Session(engine)
    try:
        yield session
    except:  # noqa B901
        session.rollback()
        raise
    finally:
        session.close()
