from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from url_shortener_db.utils import create_session


Base = declarative_base()
session = create_session()


class URL(Base):
    __tablename__ = 'URL'
    id = Column(Integer, primary_key=True)
    short_url = Column(String, nullable=False)
    long_url = Column(String, nullable=False)
    
    def __str__(self):
        return f'URL {self.id}'
