from sqlalchemy import Column, Integer, String

from infra.configs.base import Base


class Films(Base):
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    gender = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return self.title
