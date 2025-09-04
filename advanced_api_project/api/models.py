from django.db import models

class Author(models.Model):
    """
    Author model stores the name of each author.
    """
    name = models.CharField(max_length=200)

class Book(models.Model):
    """
    Book model stores book details and links each book to an author.
    The 'author' field establishes a one-to-many relationship (one author, many books).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')