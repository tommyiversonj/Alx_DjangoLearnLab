# Create Operation
from bookshelf.models import Book
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1.id)
print(book1.title)
