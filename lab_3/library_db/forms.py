from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','genre','publisher','publish_date','page_count','country','total']