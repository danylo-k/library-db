from django.contrib import admin

from .models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
admin.site.register(Reader)
admin.site.register(Country)
admin.site.register(Loan)
admin.site.register(Publisher)
admin.site.register(Genre)