from library_db.models import Author
from library_db.repositories.BaseRepository import BaseRepository

class AuthorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Author)