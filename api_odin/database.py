from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from api_odin.settings import Settings




def get_session():  # pragma: no cover
    
    with Session(engine) as session:
        yield session
