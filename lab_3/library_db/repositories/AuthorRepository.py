from library_db.models import Author, Country

class AuthorRepository:
    def get_all(self):
        return Author.objects.all()
    def get_by_id(self, author_id):
        try:
            return Author.objects.get(author_id=author_id)
        except Author.DoesNotExist:
            return None
    def add(self, first_name, last_name, middle_name, date_of_birth, date_of_death, country):
        try:
            country=Country.objects.get(country_id=country)
        except Country.DoesNotExist:
            raise ValueError("Country does not exist")
        author=Author(first_name=first_name, last_name=last_name, middle_name=middle_name, date_of_birth=date_of_birth, date_of_death=date_of_death, country=country)
        author.save()
        return author
