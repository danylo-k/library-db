from library_db.repositories.unit_of_work import UnitOfWork
from datetime import date, timedelta, datetime
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **options):
        uow=UnitOfWork()
        country1=uow.countries.get_by_id(2)
        if country1 is None:
            print("No country found")
        else:
            print(f"ID: {country1.country_id} Name: {country1.name}")
        country2=uow.countries.get_by_id(5)
        if country2 is None:
            print("No country found")
        else:
            print(f"ID: {country2.country_id} Name: {country2.name}")
        all_countries=uow.countries.get_all()
        for c in all_countries:
            print(f"ID: {c.country_id} Name: {c.name}")
        # uow.countries.add('France')
        author1=uow.authors.get_by_id(2)
        if author1 is None:
            print("No author found")
        else:
            print(f"ID: {author1.author_id}, First name: {author1.first_name}, Last name: {author1.last_name}, Middle name: {author1.middle_name}, Date of birth: {author1.date_of_birth}, Date of death: {author1.date_of_death}, Country ID: {author1.country_id}")
        author2=uow.authors.get_by_id(6)
        if author2 is None:
            print("No author found")
        else:
            print(f"ID: {author2.author_id}, First name: {author2.first_name}, Last name: {author2.last_name}, Middle name: {author2.middle_name}, Date of birth: {author2.date_of_birth}, Date of death: {author2.date_of_death}, Country ID: {author2.country_id}")
        all_authors=uow.authors.get_all()
        for a in all_authors:
            print(f"ID: {a.author_id}, First name: {a.first_name}, Last name: {a.last_name}, Middle name: {a.middle_name}, Date of birth: {a.date_of_birth}, Date of death: {a.date_of_death}, Country ID: {a.country_id}")
        # uow.authors.add('Oksana', 'Zabuzhko', 'Stefanivna', datetime(1960,9,19), None, 1)
        loan1=uow.loans.get_by_id(2)
        if loan1 is None:
            print("No loan found")
        else:
            print(f"ID: {loan1.loan_id}, Book: {loan1.book_id}, Reader: {loan1.reader_id}, Loan Date: {loan1.loan_date}, Return Date: {loan1.return_date}, Due Date: {loan1.due_date}, Status: {loan1.status}")
        loan2=uow.loans.get_by_id(5)
        if loan2 is None:
            print("No loan found")
        else:
            print(f"ID: {loan2.loan_id}, Book: {loan2.book_id}, Reader: {loan2.reader_id}, Loan Date: {loan2.loan_date}, Return Date: {loan2.return_date}, Due Date: {loan2.due_date}, Status: {loan2.status}")
        all_loans=uow.loans.get_all()
        for l in all_loans:
            print(f"ID: {l.loan_id}, Book: {l.book_id}, Reader: {l.reader_id}, Loan Date: {l.loan_date}, Return Date: {l.return_date}, Due Date: {l.due_date}, Status: {l.status}")
        # uow.loans.add(4, 5, datetime(2025,10,25), None, datetime(2025,11,25), 'not returned')