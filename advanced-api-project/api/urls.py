from django.urls import path
from .views import BookListCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URL for listing all books and creating a new one
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # URL for retrieving a single book by its primary key
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # URL for updating a book by its primary key
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # URL for deleting a book by its primary key
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
