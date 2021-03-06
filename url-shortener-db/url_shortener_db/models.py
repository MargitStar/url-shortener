from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from url_shortener_db.base_62_convertion import Base62Convertion
from url_shortener_db.utils import create_session

Base = declarative_base()
session = create_session()


class URL(Base):
    __tablename__ = "URL"
    url_id = Column(BigInteger, primary_key=True, autoincrement=False)
    short_url = Column(String, nullable=False)
    long_url = Column(String, nullable=False)

    def __str__(self):
        return f"URL {self.id}"

    @classmethod
    def get_by_short_url(cls, short_url):
        url_id = cls._decode_short_url(short_url)
        return session.query(cls).filter_by(url_id=url_id).first()

    @classmethod
    def add(cls, long_url):
        url_id = cls._generate_id()
        url_entity = cls(
            long_url=long_url,
            short_url=cls._encode_short_url(url_id),
            url_id=url_id,
        )
        session.add(url_entity)
        session.commit()
        return url_entity

    @staticmethod
    def _generate_id():
        date = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        return int(date.timestamp() * 1000)

    @staticmethod
    def _encode_short_url(url_id):
        converter = Base62Convertion()
        return converter.encode(url_id)

    @staticmethod
    def _decode_short_url(short_url):
        converter = Base62Convertion()
        return converter.decode(short_url)
