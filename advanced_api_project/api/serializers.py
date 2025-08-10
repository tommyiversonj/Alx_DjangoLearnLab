from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    - Includes custom validation: publication_year cannot be in the future.
    - 'author' field is the author's id (foreign key) here.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Field-level validation for publication_year.
        Ensures the year is not greater than the current calendar year.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "publication_year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and nests the author's books using BookSerializer.
    - 'books' is read_only and uses the related_name='books' from Book.author.
    - This provides a dynamic nested representation of the Author -> Books relationship.
    """
    books = BookSerializer(many=True, read_only=True)  # uses Author.books queryset

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
