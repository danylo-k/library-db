from library_db.models import Genre

class GenreRepository:
    def get_all(self):
        return Genre.objects.all()
    def get_by_id(self, genre_id):
        try:
            return Genre.objects.get(genre_id=genre_id)
        except Genre.DoesNotExist:
            return None
    def add_genre(self, genre_name):
        genre=Genre(name=genre_name)
        genre.save()
        return genre