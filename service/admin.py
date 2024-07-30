from django.contrib import admin
from service.models import Book, Payment, Borrowing

# Register your models here.
admin.site.register(Book)
admin.site.register(Payment)
admin.site.register(Borrowing)

