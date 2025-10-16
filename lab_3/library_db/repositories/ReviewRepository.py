from library_db.models import Review, Book, Reader

class ReviewRepository:
    def get_all(self):
        return Review.objects.all()
    def get_by_id(self, review_id):
        try:
            return Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            return None
    def add(self, book, reader, rating, text, date):
        try:
            book=Book.objects.get(book_id=book)
        except Book.DoesNotExist:
            raise ValueError("Book does not exist")
        try:
            reader=Reader.objects.get(reader_id=reader)
        except Reader.DoesNotExist:
            raise ValueError("Reader does not exist")
        review=Review(book, reader, rating, text, date)
        review.save()
        return review

