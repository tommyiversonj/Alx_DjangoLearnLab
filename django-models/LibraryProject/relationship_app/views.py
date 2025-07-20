from django.views.generic import DetailView
from django.shortcuts import render
from .models import Book

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ required
    context_object_name = 'library'  # ✅ required

def list_books(request):
    books = Book.objects.all()  # ✅ required
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ required
