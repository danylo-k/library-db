from library_db.models import Publisher

class PublisherRepository:
    def get_all(self):
        return Publisher.objects.all()
    def get_by_id(self, publisher_id):
        try:
            return Publisher.objects.get(publisher_id=publisher_id)
        except Publisher.DoesNotExist:
            return None
    def add(self, name, address, phone_number, email):
        publisher=Publisher(name=name, address=address, phone_number=phone_number, email=email)
        publisher.save()
        return publisher
