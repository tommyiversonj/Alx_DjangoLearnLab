from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author who can write multiple books.
    """
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    """
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"