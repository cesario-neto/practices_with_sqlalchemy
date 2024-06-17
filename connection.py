import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

engine = create_engine(f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
conn = engine.connect()
try:
    response = conn.execute(text('select * from films;'))
    for row in response:
        for col in row:
            print(col)
        print(row)

except Exception as e:
    print(e)
finally:
    conn.close()