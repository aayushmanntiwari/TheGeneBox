from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Authors,Books
class AuthorsModelAdmin(ModelAdmin):
    list_display = ['first_name','last_name']
class BooksModelAdmin(ModelAdmin):
    list_display = ['book_name','book_genre','author']

# Register your models here.
admin.site.register(Authors,AuthorsModelAdmin)
admin.site.register(Books,BooksModelAdmin)