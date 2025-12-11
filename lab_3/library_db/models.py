from django.db import models

class Country(models.Model):
    country_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        managed=False
        db_table='country'

class Genre(models.Model):
    genre_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed=False
        db_table='genre'

class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50, blank=True, null=True)
    date_of_birth=models.DateField()
    date_of_death=models.DateField(blank=True, null=True)
    country=models.ForeignKey(Country,models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        managed=False
        db_table='author'

class Publisher(models.Model):
    publisher_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100, blank=True, null=True)
    phone_number=models.CharField(max_length=20, blank=True, null=True)
    email=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed=False
        db_table='publisher'

class Reader(models.Model):
    reader_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50, blank=True, null=True)
    birth_date=models.DateField(blank=True, null=True)
    phone_number=models.CharField(max_length=20, blank=True, null=True)
    email=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    class Meta:
        managed=False
        db_table='reader'


class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=80)
    genre=models.ForeignKey(Genre, models.CASCADE, blank=True, null=True)
    author=models.ForeignKey(Author, models.CASCADE, blank=True, null=True)
    publisher= models.ForeignKey(Publisher, models.CASCADE, blank=True, null=True)
    publish_date=models.DateField(blank=True, null=True)
    page_count=models.IntegerField(blank=True, null=True)
    country=models.ForeignKey(Country, models.CASCADE, blank=True, null=True)
    total=models.IntegerField(blank=True, null=True)
    available=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        managed=False
        db_table='book'

class Loan(models.Model):
    loan_id=models.AutoField(primary_key=True)
    book=models.ForeignKey(Book, models.CASCADE)
    reader=models.ForeignKey(Reader, models.CASCADE)
    loan_date=models.DateField()
    return_date=models.DateField(blank=True, null=True)
    due_date=models.DateField()
    status=models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        managed=False
        db_table='loan'

class Review(models.Model):
    review_id=models.AutoField(primary_key=True)
    book=models.ForeignKey(Book, models.CASCADE)
    reader=models.ForeignKey(Reader, models.CASCADE)
    rating=models.IntegerField()
    text=models.CharField(max_length=1000, blank=True, null=True)
    date=models.DateField()
    class Meta:
        managed=False
        db_table='review'