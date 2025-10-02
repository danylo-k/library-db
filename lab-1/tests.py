import datetime
class Book:
    def __init__(self, title, author, pages):
        self.__title=title
        self.__author=author
        self.__pages=int(pages)
    def get_pages(self):
        return self.__pages
    def set_pages(self, pages):
        self.__pages=pages
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title=title
    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author=author
    @staticmethod
    def create_book(string):
        title,author,pages=string.split(';')
        return Book(title,author,pages)
class Person:
    def __init__(self, first_name, last_name, middle_name, birth_date):
        self.first_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name
        self.birth_date=birth_date
    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"
    def get_age(self):
        today=datetime.date.today()
        return today.year-self.birth_date.year-((today.month,today.day) < (self.birth_date.month,self.birth_date.day))
class Author(Person):
    def __init__(self, first_name, last_name, middle_name, birth_date, death_date):
        Person.__init__(self, first_name, last_name, middle_name, birth_date)
        self.death_date=death_date
    def get_age(self):
        if self.death_date is None:
            return super().get_age()
        return self.death_date.year-self.birth_date.year-((self.death_date.month, self.death_date.day)<(self.birth_date.month, self.birth_date.day))
class LibraryUser:
    def __init__(self, card_number):
        self.card_number=card_number
class Reader(Person, LibraryUser):
    def __init__(self, first_name, last_name, middle_name, birth_date, card_number):
        Person.__init__(self, first_name, last_name, middle_name, birth_date)
        LibraryUser.__init__(self, card_number)
        self.books_taken=[]
    def take_book(self, book):
        if book in self.books_taken:
            print("This book is already taken.")
            return
        print(f"Taking {book.get_title()}")
        self.books_taken.append(book)
    def return_book(self, book):
        if book in self.books_taken:
            print(f"Returning {book.get_title()}")
            self.books_taken.remove(book)
        else:
            print("You don't have this book!")
b1 = Book("1984","George Orwell",328)
print(b1.get_title())
print(b1.get_author())
print(b1.get_pages())
b1.set_title("Animal Farm")
b1.set_author("Orwell")
b1.set_pages(112)
print(b1.get_title(),b1.get_author(),b1.get_pages())
b2=Book.create_book("Brave New World;Aldous Huxley;311")
print(b2.get_title(),b2.get_author(),b2.get_pages())
p=Person("Ivan","Petrenko","Ivanovych",datetime.date(2000,5,20))
print(p.get_full_name())
print(p.get_age())
a1=Author("Lesya","Ukrainka","Petrivna",datetime.date(1871,2,25),datetime.date(1913,8,1))
print(a1.get_full_name(),a1.get_age())
a2=Author("Oksana","Zabuzhko","Stefanivna",datetime.date(1960,9,19),None)
print(a2.get_full_name(),a2.get_age())
reader=Reader("Oleh","Ivanov","Petrovych",datetime.date(2001,7,15),"12345")
print(reader.get_full_name(),reader.get_age())
reader.take_book(b1)
reader.take_book(b1)
reader.take_book(b2)
reader.return_book(b1)
reader.return_book(b1)
reader.return_book(b2)