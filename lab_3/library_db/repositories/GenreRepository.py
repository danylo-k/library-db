from library_db.models import Genre
from library_db.repositories.BaseRepository import BaseRepository

class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__(Genre)