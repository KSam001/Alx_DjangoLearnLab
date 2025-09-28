from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    This view handles listing all books and creating a new book.
    - GET: Lists all books.
    - POST: Creates a new book instance.
    Requires authentication for creation, but allows read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    This view handles retrieving a single book instance by its ID.
    - GET: Retrieves a single book.
    Allows read-only access for all users, regardless of authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    """
    This view handles updating an existing book.
    - PUT/PATCH: Updates a book instance.
    Requires authentication for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    """
    This view handles deleting a book instance.
    - DELETE: Deletes a book instance.
    Restricts access to only admin users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
