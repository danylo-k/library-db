from library_db.models import Reader
from library_db.repositories.BaseRepository import BaseRepository

class ReaderRepository(BaseRepository):
    def __init__(self):
        super().__init__(Reader)