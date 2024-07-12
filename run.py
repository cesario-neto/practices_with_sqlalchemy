from dotenv import load_dotenv

from infra.repository.films_repository import FilmsRepository

load_dotenv()

repo = FilmsRepository()

data = repo.select()
print(data)

repo.insert('test', 'test', 2002)
data = repo.select()
print(data)

repo.update('test', 'Any')
data = repo.select()
print(data)

repo.delete('test')
data = repo.select()
print(data)
