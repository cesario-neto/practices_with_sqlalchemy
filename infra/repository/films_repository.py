from infra.configs.connection import DBConnectionHandler
from infra.entities.films import Films


class FilmsRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Films).all()
            return data

    def insert(self, title, gender, year):
        with DBConnectionHandler() as db:
            data_insert = Films(
                title=title, gender=gender, year=year)
            db.session.add(data_insert)
            db.session.commit()

    def update(self, title, gender):
        with DBConnectionHandler() as db:
            db.session.query(Films).filter(
                Films.title == title).update({'gender': gender})

            db.session.commit()

    def delete(self, title):
        with DBConnectionHandler() as db:
            db.session.query(Films).filter(Films.title == title).delete()
            db.session.commit()
