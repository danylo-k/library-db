from library_db.models import *

class ReportRepository():
    def report(self):
        data = {
            "total_books": Book.objects.count(),
            "total_authors": Author.objects.count(),
            "total_readers": Reader.objects.count(),
            "total_publishers": Publisher.objects.count(),
            "total_loans": Loan.objects.count(),
            "total_reviews": Review.objects.count(),
            "total_countries": Country.objects.count(),
            "genres": list(Genre.objects.values_list("name", flat=True))
        }
        return data