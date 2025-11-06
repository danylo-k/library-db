from library_db.models import Country
from library_db.repositories.BaseRepository import BaseRepository

class CountryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Country)