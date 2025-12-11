import pandas as pd
import requests
from django.db.models import Count, Avg, Value
from django.db.models.functions import TruncMonth, Concat
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from numpy.linalg.lapack_lite import dgelsd

from .forms import BookForm
from .repositories.unit_of_work import UnitOfWork
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
import plotly.io as pio
import plotly.express as px
from rest_framework.views import APIView
# Create your views here.

uow=UnitOfWork()
# Country
class CountryListView(APIView):
    def get(self,request):
        countries=uow.countries.get_all()
        serializer=CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=CountrySerializer(data=request.data)
        if serializer.is_valid():
            country=uow.countries.add(**serializer.validated_data)
            return Response(CountrySerializer(country).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetailedView(APIView):
    def get(self,request,pk):
        try:
            country=uow.countries.get_by_id(pk)
            serializer=CountrySerializer(country)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_404_NOT_FOUND)
    def patch(self,request,pk):
        try:
            country=uow.countries.update(pk, **request.data)
            if country:
                serializer=CountrySerializer(country)
                return Response(serializer.data)
            return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        country=uow.countries.delete(pk)
        if country:
            return Response({"message": "Country deleted"})
        return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)
# Author
class AuthorListView(APIView):
    def get(self,request):
        authors=uow.authors.get_all()
        serializer=AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            author=uow.authors.add(**serializer.validated_data)
            return Response(AuthorSerializer(author).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailedView(APIView):
    def get(self,request,pk):
        try:
            author=uow.authors.get_by_id(pk)
            serializer=AuthorSerializer(author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_404_NOT_FOUND)
    def patch(self,request,pk):
        try:
            author=uow.authors.update(pk, **request.data)
            if author:
                serializer=AuthorSerializer(author)
                return Response(serializer.data)
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        author=uow.authors.delete(pk)
        if author:
            return Response({"message": "Author deleted"})
        return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
# Book
class BookListView(APIView):
    def get(self,request):
        books=uow.books.get_all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            book=uow.books.add(**serializer.validated_data)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailedView(APIView):
    def get(self,request,pk):
        try:
            book=uow.books.get_by_id(pk)
            serializer=BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_404_NOT_FOUND)
    def patch(self,request,pk):
        try:
            book=uow.books.update(pk, **request.data)
            if book:
                serializer=BookSerializer(book)
                return Response(serializer.data)
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        book=uow.books.delete(pk)
        if book:
            return Response({"message": "Book deleted"})
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
# Genre
class GenreListView(APIView):
    def get(self, request):
        genres=uow.genres.get_all()
        serializer=GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=GenreSerializer(data=request.data)
        if serializer.is_valid():
            genre=uow.genres.add(**serializer.validated_data)
            return Response(GenreSerializer(genre).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenreDetailedView(APIView):
    def get(self,request,pk):
        try:
            genre=uow.genres.get_by_id(pk)
            if genre:
                serializer = GenreSerializer(genre)
                return Response(serializer.data)
            return Response({"error": "Genre not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            genre=uow.genres.update(pk, **request.data)
            if genre:
                serializer=GenreSerializer(genre)
                return Response(serializer.data)
            return Response({"error": "Genre not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        genre=uow.genres.delete(pk)
        if genre:
            return Response({"message": "Genre deleted"})
        return Response({"error": "Genre not found"}, status=status.HTTP_404_NOT_FOUND)
# Loan
class LoanListView(APIView):
    def get(self,request):
        loans=uow.loans.get_all()
        serializer=LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=LoanSerializer(data=request.data)
        if serializer.is_valid():
            loan=uow.loans.add(**serializer.validated_data)
            return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetailedView(APIView):
    def get(self,request,pk):
        try:
            loan=uow.loans.get_by_id(pk)
            if loan:
                serializer=LoanSerializer(loan)
                return Response(serializer.data)
            return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            loan=uow.loans.update(pk, **request.data)
            if loan:
                serializer=LoanSerializer(loan)
                return Response(serializer.data)
            return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        loan=uow.loans.delete(pk)
        if loan:
            return Response({"message": "Loan deleted"})
        return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
# Publisher
class PublisherListView(APIView):
    def get(self,request):
        publishers=uow.publishers.get_all()
        serializer=PublisherSerializer(publishers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=PublisherSerializer(data=request.data)
        if serializer.is_valid():
            publisher=uow.publishers.add(**serializer.validated_data)
            return Response(PublisherSerializer(publisher).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublisherDetailedView(APIView):
    def get(self,request,pk):
        try:
            publisher=uow.publishers.get_by_id(pk)
            if publisher:
                serializer=PublisherSerializer(publisher)
                return Response(serializer.data)
            return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            publisher=uow.publishers.update(pk, **request.data)
            if publisher:
                serializer=PublisherSerializer(publisher)
                return Response(serializer.data)
            return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        publisher=uow.publishers.delete(pk)
        if publisher:
            return Response({"message": "Publisher deleted"})
        return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)
# Reader
class ReaderListView(APIView):
    def get(self,request):
        readers=uow.readers.get_all()
        serializer=ReaderSerializer(readers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=ReaderSerializer(data=request.data)
        if serializer.is_valid():
            reader=uow.readers.add(**serializer.validated_data)
            return Response(ReaderSerializer(reader).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReaderDetailedView(APIView):
    def get(self,request,pk):
        try:
            reader=uow.readers.get_by_id(pk)
            if reader:
                serializer=ReaderSerializer(reader)
                return Response(serializer.data)
            return Response({"error": "Reader not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            reader=uow.readers.update(pk, **request.data)
            if reader:
                serializer=ReaderSerializer(reader)
                return Response(serializer.data)
            return Response({"error": "Reader not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        reader=uow.readers.delete(pk)
        if reader:
            return Response({"message": "Reader deleted"})
        return Response({"error": "Reader not found"}, status=status.HTTP_404_NOT_FOUND)
# Review
class ReviewListView(APIView):
    def get(self,request):
        reviews=uow.reviews.get_all()
        serializer=ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review=uow.reviews.add(**serializer.validated_data)
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailedView(APIView):
    def get(self,request,pk):
        try:
            review=uow.reviews.get_by_id(pk)
            if review:
                serializer=ReviewSerializer(review)
                return Response(serializer.data)
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            review=uow.reviews.update(pk, **request.data)
            if review:
                serializer=ReviewSerializer(review)
                return Response(serializer.data)
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        review=uow.reviews.delete(pk)
        if review:
            return Response({"message": "Review deleted"})
        return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
# report
class ReportView(APIView):
    def get(self, request):
        reports=uow.report.report()
        return Response(reports, status=status.HTTP_200_OK)

class IndexView(ListView):
    template_name = 'library_db/index.html'
    context_object_name = 'books_list'
    def get_queryset(self):
        return Book.objects.all()
class BookDetailView(DetailView):
    model = Book
    template_name = 'library_db/book_detail.html'
    context_object_name = 'book'

def create_book(request):
    form=BookForm()
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "library_db/create_book.html", {"form":form})
def edit_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    if request.method=="POST":
        form=BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book-detail", pk=pk)
    else:
        form=BookForm(instance=book)
    return render(request, "library_db/edit_book.html", {"form": form, "book": book})
def delete_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    if request.method=="POST":
        book.delete()
        return redirect("books")  # your book list URL name
    return render(request,"library_db/delete_book.html", {"book": book})
def course_list(request):
    response=requests.request("GET", 'http://127.0.0.1:8003/api/courses/', headers={'Content-Type': 'application/json'}, auth=('dector', 'itsamemario'))
    if response.status_code==200:
        courses=response.json()
    else:
        courses=[]
    return render(request, 'library_db/courses_list.html', {'courses':courses})
def course_detail(request,course_id):
    response=requests.request("GET", f'http://127.0.0.1:8003/api/courses/{course_id}',auth=('dector', 'itsamemario'))
    if response.status_code==200:
        course=response.json()
    else:
        course=None
    return render(request, 'library_db/course_detail.html', {'course':course})
def course_delete(request,course_id):
    response=requests.get(f'http://127.0.0.1:8003/api/courses/{course_id}',auth=('dector', 'itsamemario'))
    course=response.json()
    if request.method=="POST":
        requests.request("DELETE",f'http://127.0.0.1:8003/api/courses/{course_id}/',headers={'Content-Type': 'application/json'},auth=('dector', 'itsamemario'))
        return redirect("course-list")
    return render(request,'library_db/delete_course.html', {'course':course})
def books_by_genre(request):
    data=list(
            Genre.objects.annotate(
            book_count=Count('book')
        ).values('name', 'book_count')
    )
    return JsonResponse(data, safe=False)
def avg_author_rating(request):
    data=list(
        Author.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            avg_rating=Avg('book__review__rating')
        )
        .order_by('avg_rating')
        .values('full_name', 'avg_rating')
    )
    return JsonResponse(data, safe=False)
def authors_by_country(request):
    data=list(
        Country.objects.annotate(author_count=Count('author')).values('name','author_count')
    )
    return JsonResponse(data, safe=False)
def loan_count_by_reader(request):
    data=list(
        Reader.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        )
        .annotate(loan_count=Count('loan'))
        .values('full_name', 'loan_count')
    )
    return JsonResponse(data, safe=False)
def loans_per_month(request):
    data=list(
        Loan.objects.annotate(month=TruncMonth('loan_date')).values('month').annotate(count=Count('loan_id'))
    )
    return JsonResponse(data, safe=False)
def top_authors_by_books(request):
    data = list(
        Author.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            book_count=Count('book')
        )
        .order_by('-book_count')
        .values('full_name', 'book_count')
    )
    return JsonResponse(data, safe=False)

class Dashboardv1(View):
    def get(self,request):
        qs_1=requests.get('http://localhost:8000/books-by-genre/')
        df_1=pd.DataFrame(qs_1.json())
        if not df_1.empty:
            fig1=px.bar(df_1, x='name',y='book_count',title='Books counted by genre')
        else:
            fig1=px.bar(title='No data')
        graph1=pio.to_html(fig1, full_html=False)
        qs_2=requests.get('http://localhost:8000/average-author-rating/')
        df_2=pd.DataFrame(qs_2.json())
        if not df_2.empty:
            fig2=px.scatter(df_2, x='full_name', y='avg_rating', title='Average rating by author')
        else:
            fig2=px.scatter(title='No data')
        graph2=pio.to_html(fig2, full_html=False)
        qs_3=requests.get('http://localhost:8000/authors-by-country/')
        df_3 = pd.DataFrame(qs_3.json())
        if not df_3.empty:
            fig3 = px.pie(df_3, values='author_count', names='name', title='Author by country')
        else:
            fig3 = px.pie(title='No data')
        graph3 = pio.to_html(fig3, full_html=False)
        qs_4=requests.get('http://localhost:8000/loans-by-reader/')
        df_4=pd.DataFrame(qs_4.json())
        if not df_4.empty:
            fig4 = px.scatter(df_4, x='full_name', y='loan_count', title='Loans by reader')
        else:
            fig4 = px.scatter(title='No data')
        graph4 = pio.to_html(fig4, full_html=False)
        qs_5=requests.get('http://localhost:8000/loans-per-month/')
        df_5=pd.DataFrame(qs_5.json())
        if not df_5.empty:
            fig5 = px.scatter(df_5, x='month', y='count', title='Loans by month')
        else:
            fig5 = px.scatter(title='No data')
        graph5 = pio.to_html(fig5, full_html=False)
        qs_6=requests.get('http://localhost:8000/top-authors/')
        df_6=pd.DataFrame(qs_6.json())
        if not df_6.empty:
            fig6=px.bar(df_6, x='full_name', y='book_count', title='Most books written by author')
        else:
            fig6=px.bar(title='No data')
        graph6 = pio.to_html(fig6, full_html=False)
        context={
            'graph1': graph1,
            'graph2': graph2,
            'graph3': graph3,
            'graph4': graph4,
            'graph5': graph5,
            'graph6': graph6
        }
        return render(request,'library_db/dashboard_v1.html',context)