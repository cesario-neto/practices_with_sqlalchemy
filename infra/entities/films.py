from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from infra.configs.base import Base


class Films(Base):
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    gender = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    actors = relationship('Actors', backref='actors', lazy='subquery')

    def __repr__(self):
        return self.title
