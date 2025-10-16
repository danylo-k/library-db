from library_db.models import Country

class CountryRepository:
    def get_all(self):
        return Country.objects.all()
    def get_by_id(self, country_id):
        try:
            return Country.objects.get(country_id=country_id)
        except Country.DoesNotExist:
            return None
    def add(self, country_name):
        country=Country(name=country_name)
        country.save()
        return country