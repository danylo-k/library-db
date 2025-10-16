from library_db.models import Loan, Book, Reader

class LoanRepository:
    def get_all(self):
        return Loan.objects.all()
    def get_by_id(self, loan_id):
        try:
            return Loan.objects.get(loan_id=loan_id)
        except Loan.DoesNotExist:
            return None
    def add(self, book, reader, loan_date, return_date, due_date, status):
        try:
            book=Book.objects.get(book_id=book)
        except Book.DoesNotExist:
            raise ValueError("Book does not exist")
        try:
            reader=Reader.objects.get(reader_id=reader)
        except Reader.DoesNotExist:
            raise ValueError("Reader does not exists")
        loan=Loan(book=book, reader=reader, loan_date=loan_date, return_date=return_date, due_date=due_date, status=status)
        loan.save()
        return loan

