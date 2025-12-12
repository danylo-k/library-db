import pandas as pd
import requests
from django.db.models import Count, Avg, Value
from django.db.models.functions import TruncMonth, Concat
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from numpy.linalg.lapack_lite import dgelsd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.transform import cumsum
from math import pi
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
    df = pd.DataFrame(data)
    return HttpResponse(df.to_dict())
def avg_author_rating(request):
    data=list(
        Author.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            avg_rating=Avg('book__review__rating')
        )
        .order_by('avg_rating')
        .values('full_name', 'avg_rating')
    )
    df=pd.DataFrame(data)
    return HttpResponse(df.to_dict())
def authors_by_country(request):
    data=list(
        Country.objects.annotate(author_count=Count('author')).values('name','author_count')
    )
    df = pd.DataFrame(data)
    return HttpResponse(df.to_dict())
def loan_count_by_reader(request):
    data=list(
        Reader.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        )
        .annotate(loan_count=Count('loan'))
        .values('full_name', 'loan_count')
    )
    df=pd.DataFrame(data)
    return HttpResponse(df.to_dict())
def loans_per_month(request):
    data=list(
        Loan.objects.annotate(month=TruncMonth('loan_date')).values('month').annotate(count=Count('loan_id'))
    )
    df = pd.DataFrame(data)
    return HttpResponse(df.to_dict())
def top_authors_by_books(request):
    data = list(
        Author.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            book_count=Count('book')
        )
        .order_by('-book_count')
        .values('full_name', 'book_count')
    )
    df=pd.DataFrame(data)
    return HttpResponse(df.to_dict())
def book_page_stats(request):
    data=list(
        Book.objects.all().values("title", "page_count")
    )
    df=pd.DataFrame(data)
    stats = {
        "mean_pages": int(df["page_count"].mean()),
        "median_pages": int(df["page_count"].median()),
        "max_pages": int(df["page_count"].max()),
        "min_pages": int(df["page_count"].min())
    }
    return JsonResponse(stats)
def rating_by_page_group(request):
    small = Review.objects.filter(
        book_id__page_count__lt=250
    ).aggregate(avg_rating=Avg("rating"))["avg_rating"]
    large=Review.objects.filter(
        book_id__page_count__gte=250
    ).aggregate(avg_rating=Avg("rating"))["avg_rating"]
    stats={
        "avg_rating_pages_lt_250": small,
        "avg_rating_pages_gte_250": large,
        "review_count_lt_250": Review.objects.filter(book_id__page_count__lt=250).count(),
        "review_count_gte_250": Review.objects.filter(book_id__page_count__gte=250).count()
    }
    return JsonResponse(stats)
class Dashboardv1(View):
    def get(self,request):
        min_books=int(request.GET.get('min_books',1))
        qs_1=(
            Genre.objects.annotate(
                book_count=Count('book')
            ).filter(book_count__gte=min_books).values('name', 'book_count')
        )
        df_1=pd.DataFrame(list(qs_1))
        if not df_1.empty:
            fig1=px.bar(df_1, x='name',y='book_count',title='Books counted by genre')
        else:
            fig1=px.bar(title='No data')
        graph1=pio.to_html(fig1, full_html=False)
        min_rating=float(request.GET.get('min_rating',1))
        qs_2=(
        Author.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            avg_rating=Avg('book__review__rating')
        )
        .filter(avg_rating__gte=min_rating)
        .order_by('avg_rating')
        .values('full_name', 'avg_rating')
        )
        df_2=pd.DataFrame(list(qs_2))
        if not df_2.empty:
            fig2=px.scatter(df_2, x='full_name', y='avg_rating', title='Average rating by author')
        else:
            fig2=px.scatter(title='No data')
        graph2=pio.to_html(fig2, full_html=False)
        qs_3 = (
                Country.objects.annotate(author_count=Count('author')).values('name','author_count')
        )
        df_3 = pd.DataFrame(list(qs_3))
        if not df_3.empty:
            fig3 = px.pie(df_3, values='author_count', names='name', title='Author by country')
        else:
            fig3 = px.pie(title='No data')
        graph3 = pio.to_html(fig3, full_html=False)
        qs_4 = (
            Reader.objects.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name')
            )
            .annotate(loan_count=Count('loan'))
            .values('full_name', 'loan_count')
        )
        df_4 = pd.DataFrame(list(qs_4))
        if not df_4.empty:
            fig4 = px.scatter(df_4, x='full_name', y='loan_count', title='Loans by reader')
        else:
            fig4 = px.scatter(title='No data')
        graph4 = pio.to_html(fig4, full_html=False)
        qs_5=(
            Loan.objects.annotate(month=TruncMonth('loan_date')).values('month').annotate(count=Count('loan_id'))
        )
        df_5=pd.DataFrame(list(qs_5))
        if not df_5.empty:
            fig5 = px.scatter(df_5, x='month', y='count', title='Loans by month')
        else:
            fig5 = px.scatter(title='No data')
        graph5 = pio.to_html(fig5, full_html=False)
        qs_6=(
            Author.objects.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name'),
                book_count=Count('book')
            ).order_by('-book_count').values('full_name', 'book_count')
        )
        df_6=pd.DataFrame(list(qs_6))
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
class Dashboardv2(View):
    def get(self, request):
        try:
            min_books=int(request.GET.get('min_books', 1))
        except (TypeError, ValueError):
            min_books=1
        qs_1=(
            Genre.objects.annotate(book_count=Count('book'))
            .filter(book_count__gte=min_books)
            .values('name', 'book_count')
        )
        df_1=pd.DataFrame(list(qs_1))
        if not df_1.empty:
            source1=ColumnDataSource(df_1)
            fig1=figure(x_range=df_1['name'], height=350, title="Books counted by genre")
            fig1.vbar(x='name', top='book_count', width=0.9, source=source1)
            fig1.xaxis.major_label_orientation=pi/4
        else:
            fig1=figure(title="No data")
        script1,div1=components(fig1)
        try:
            min_rating = float(request.GET.get('min_rating', 1))
        except (TypeError, ValueError):
            min_rating=1
        qs_2 = (
            Author.objects.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name'),
                avg_rating=Avg('book__review__rating')
            )
            .filter(avg_rating__gte=min_rating)
            .order_by('avg_rating')
            .values('full_name', 'avg_rating')
        )
        df_2 = pd.DataFrame(list(qs_2))
        if not df_2.empty:
            source2=ColumnDataSource(df_2)
            fig2=figure(x_range=df_2['full_name'], height=350, title="Average rating by author")
            fig2.scatter(x='full_name', y='avg_rating', size=10, source=source2)
            fig2.xaxis.major_label_orientation = pi/4
        else:
            fig2 = figure(title="No data")
        script2, div2 = components(fig2)
        qs_3 = Country.objects.annotate(author_count=Count('author')).values('name','author_count')
        df_3 = pd.DataFrame(list(qs_3))
        if not df_3.empty:
            df_3['angle'] = df_3['author_count']/df_3['author_count'].sum()*2*pi
            df_3['color'] = ["#f46642", "#42f4a8", "#4287f4", "#f4e142", "#a142f4"]
            source3 = ColumnDataSource(df_3)
            fig3 = figure(height=600, title="Authors by country", toolbar_location=None,
                          tools="hover", tooltips="@name: @author_count")
            fig3.wedge(x=1, y=0, radius=0.2,
                       start_angle=cumsum('angle', include_zero=True),
                       end_angle=cumsum('angle'),
                       line_color="white", fill_color='color', source=source3)
            fig3.axis.visible=False
            fig3.grid.visible=False
        else:
            fig3 = figure(title="No data")
        script3,div3=components(fig3)
        qs_4= (
            Reader.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
            .annotate(loan_count=Count('loan'))
            .values('full_name', 'loan_count')
        )
        df_4 = pd.DataFrame(list(qs_4))
        if not df_4.empty:
            source4 = ColumnDataSource(df_4)
            fig4=figure(x_range=df_4['full_name'], height=350, title="Loans by reader")
            fig4.scatter(x='full_name', y='loan_count', size=10, source=source4)
        else:
            fig4=figure(title="No data")

        script4, div4 = components(fig4)
        qs_5 = Loan.objects.annotate(month=TruncMonth('loan_date')).values('month').annotate(count=Count('loan_id'))
        df_5 = pd.DataFrame(list(qs_5))
        if not df_5.empty:
            source5 = ColumnDataSource(df_5)
            fig5 = figure(x_axis_type='datetime', height=350, title="Loans by month")
            fig5.scatter(x='month', y='count', source=source5)
        else:
            fig5 = figure(title="No data")
        script5, div5 = components(fig5)
        qs_6 = Author.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            book_count=Count('book')
        ).order_by('-book_count').values('full_name', 'book_count')
        df_6 = pd.DataFrame(list(qs_6))
        if not df_6.empty:
            source6 = ColumnDataSource(df_6)
            fig6=figure(x_range=df_6['full_name'], height=350, title="Most books written by author")
            fig6.vbar(x='full_name', top='book_count', width=0.9, source=source6)
        else:
            fig6 = figure(title="No data")
        script6, div6 = components(fig6)
        context = {
            'script1': script1, 'div1': div1,
            'script2': script2, 'div2': div2,
            'script3': script3, 'div3': div3,
            'script4': script4, 'div4': div4,
            'script5': script5, 'div5': div5,
            'script6': script6, 'div6': div6,
        }
        return render(request, 'library_db/dashboard_v2.html', context)