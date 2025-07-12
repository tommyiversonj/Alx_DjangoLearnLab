from bookshelf.models import Book
# Retrieve the book to be deleted (using its updated title)
book = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the object from the database
book.delete()
# Confirm deletion by trying to retrieve all books.
# This should return an empty QuerySet if no other books exist.
print(Book.objects.all())
