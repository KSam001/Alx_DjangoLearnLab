from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It includes custom validation to ensure the publication year is not in the future.
    This serializer is nested within the AuthorSerializer to display related books.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to check that the publication_year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    It demonstrates a nested relationship by including a list of the author's books.
    The 'books' field is a list of serialized Book objects.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
