from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    """
    Author model: stores the name of an author.
    Purpose:
      - Represents the "one" side of a one-to-many relationship: one Author can have many Books.
    Fields:
      - name: CharField holding the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model: stores title, publication year, and a foreign-key to Author.
    Purpose:
      - Each Book belongs to an Author, forming a one-to-many relationship (Author -> Books).
    Fields:
      - title: CharField for the book title.
      - publication_year: IntegerField for the year the book was published.
      - author: ForeignKey to Author with related_name='books' so we can access author.books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"