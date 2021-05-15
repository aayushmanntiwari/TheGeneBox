from rest_framework import serializers
from .models import Authors,Books

class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['first_name','last_name']

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['book_name','book_genre','author']