from library_db.repositories.AuthorRepository import AuthorRepository
from library_db.repositories.BookRepository import BookRepository
from library_db.repositories.CountryRepository import CountryRepository
from library_db.repositories.GenreRepository import GenreRepository
from library_db.repositories.LoanRepository import LoanRepository
from library_db.repositories.PublisherRepository import PublisherRepository
from library_db.repositories.ReaderRepository import ReaderRepository
from library_db.repositories.ReviewRepository import ReviewRepository
from library_db.repositories.ReportRepository import ReportRepository


class UnitOfWork:
    def __init__(self):
        self.authors=AuthorRepository()
        self.books=BookRepository()
        self.countries=CountryRepository()
        self.genres=GenreRepository()
        self.loans=LoanRepository()
        self.publishers=PublisherRepository()
        self.readers=ReaderRepository()
        self.reviews=ReviewRepository()
        self.report=ReportRepository()