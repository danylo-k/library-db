from library_db.models import Book, Country, Author, Genre, Publisher


class BookRepository:
    def get_all(self):
        return Book.objects.all()
    def get_by_id(self, book_id):
        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            return None
    def add(self, title, genre, author, publisher, publish_date, page_count, country, total, available):
        try:
            genre=Genre.objects.get(genre_id=genre)
        except Genre.DoesNotExist:
            genre=None
        try:
            author=Author.objects.get(author_id=author)
        except Author.DoesNotExist:
            author=None
        try:
            publisher=Publisher.objects.get(publisher_id=publisher)
        except Publisher.DoesNotExist:
            publisher=None
        try:
            country=Country.objects.get(country_id=country)
        except Country.DoesNotExist:
            country=None
        book=Book(title, genre, author, publisher, publish_date, page_count, country, total, available)
        book.save()
        return book

