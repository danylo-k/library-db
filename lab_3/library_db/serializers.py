from rest_framework import serializers
from .models import Author, Book, Country, Reader, Loan, Review, Genre, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reader
        fields='__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields='__all__'