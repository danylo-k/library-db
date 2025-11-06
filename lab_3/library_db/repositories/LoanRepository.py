from library_db.models import Loan
from library_db.repositories.BaseRepository import BaseRepository

class LoanRepository(BaseRepository):
    def __init__(self):
        super().__init__(Loan)