from bookshelf.models import Book
# Retrieve by title. For real applications, retrieving by a unique ID (primary key) is often better.
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
