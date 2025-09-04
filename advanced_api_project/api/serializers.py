from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields and validates publication_year.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate(self, data):
        """
        Ensure publication_year is not in the future.
        """
        if data['publication_year'] > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future!")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and nests related books using BookSerializer.
    The 'books' field uses the related_name on Book.author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']