from library_db.models import Publisher
from library_db.repositories.BaseRepository import BaseRepository

class PublisherRepository(BaseRepository):
    def __init__(self):
        super().__init__(Publisher)