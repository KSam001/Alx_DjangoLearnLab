from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books with filtering, searching, and ordering capabilities.
    
    - Filtering: Can filter by title, author, and publication_year.
      Example: /api/books/?publication_year=1951
    
    - Searching: Can search by title or author name.
      Example: /api/books/?search=catcher
    
    - Ordering: Can order by any field, particularly title and publication_year.
      Example: /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Configure filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Fields available for filtering
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Fields available for searching
    search_fields = ['title', 'author__name']
    
    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    Permissions: Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book.
    Permissions: Read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    Permissions: Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    Permissions: Only admin users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
