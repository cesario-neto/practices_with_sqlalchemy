from sqlalchemy import Column, ForeignKey, Integer, String

from infra.configs.base import Base


class Actors(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    film_title = Column(String, ForeignKey('films.title'))

    def __repr__(self):
        return f'{self.name} - {self.film_title}'
