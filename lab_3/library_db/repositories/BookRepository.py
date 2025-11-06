from library_db.models import Book
from library_db.repositories.BaseRepository import BaseRepository

class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(Book)