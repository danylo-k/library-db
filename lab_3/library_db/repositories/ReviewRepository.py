from library_db.models import Review
from library_db.repositories.BaseRepository import BaseRepository

class ReviewRepository(BaseRepository):
    def __init__(self):
        super().__init__(Review)