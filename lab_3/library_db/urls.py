from .views import *
from django.urls import path, include

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailedView.as_view(), name='author-detailed'),
    path('books/', IndexView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/edit/', edit_book, name='book-edit'),
    path('books/create/', create_book, name='book-create'),
    path('books/<int:pk>/delete/', delete_book, name='book-delete'),
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetailedView.as_view(), name='country-detailed'),
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailedView.as_view(), name='genre-detailed'),
    path('loans/', LoanListView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanDetailedView.as_view(), name='loan-detailed'),
    path('publishers/', PublisherListView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetailedView.as_view(), name='publisher-detailed'),
    path('readers/', ReaderListView.as_view(), name='reader-list'),
    path('readers/<int:pk>/', ReaderDetailedView.as_view(), name='reader-detailed'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailedView.as_view(), name='review-detailed'),
    path('report/', ReportView.as_view(), name='report'),
]