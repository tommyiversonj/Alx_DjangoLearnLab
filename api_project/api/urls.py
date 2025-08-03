from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookListCreateAPIView.as_view(), name="book_list_create"),
    # Note: I've added a trailing slash to "books/" which is standard Django practice.
]