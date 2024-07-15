from infra.configs.connection import DBConnectionHandler
from infra.entities.actors import Actors
from infra.entities.films import Films


class ActorsRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Actors).join(Films, Actors.film_title == Films.title).with_entities(
                Actors.name, Films.title, Films.gender).all()
            return data
