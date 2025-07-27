from bookshelf.models import Book
# Retrieve the book first
book = Book.objects.get(title="1984")
# Update an attribute
book.title = "Nineteen Eighty-Four"
# Save the changes to the database
book.save()
print(f"Updated Title: {book.title}")
