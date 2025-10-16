from library_db.models import Reader

class ReaderRepository:
    def get_all(self):
        return Reader.objects.all()
    def get_by_id(self, reader_id):
        try:
            reader=Reader.objects.get(reader_id=reader_id)
        except Reader.DoesNotExist:
            return None
    def add(self, first_name, last_name, middle_name, birth_date, phone_number, email):
        reader=Reader(first_name=first_name, last_name=last_name, middle_name=middle_name, birth_date=birth_date, phone_number=phone_number, email=email)
        reader.save()
        return reader