from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing book instances. Permissions are
    enforced based on the user's assigned group.
    - Viewers: can_view
    - Editors: can_view, can_create, can_edit
    - Admins: all permissions
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissions]
