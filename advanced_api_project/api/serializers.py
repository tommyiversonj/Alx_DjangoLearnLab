from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Validates that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes nested serialization of related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
