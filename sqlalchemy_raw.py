import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

# Settings
engine = create_engine(f'postgresql+psycopg2://{POSTGRES_USER}:{
                       POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Entities
class Films(Base):
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    gender = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return self.title

# SQL


# Delete
try:
    session.query(Films).filter(Films.title == 'Um filme').delete()
    session.commit()
except:
    ...

# Insert
data_insert = Films(title='Um filme', gender='Aventura', year='2005')
session.add(data_insert)
session.commit()

# Update
session.query(Films).filter(
    Films.title == 'Um filme').update({'gender': 'Drama'})
session.commit()

# Select
data = session.query(Films).all()
print(data)
for film in data:
    print(f'{film.title} - {film.gender} - {film.year}')


session.close()
