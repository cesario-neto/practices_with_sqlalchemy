from dotenv import load_dotenv

from infra.repository.actors_repository import ActorsRepository
from infra.repository.films_repository import FilmsRepository

load_dotenv()


repo = ActorsRepository()
data = repo.select()
print(data)

repo2 = FilmsRepository()
data2 = repo2.select()
film = data2[0].actors
print(film)
