from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Sample queries for relationship_app models'
    def handle(self, *args, **kwargs):
        try:
            # Query all books by a specific author
            author = Author.objects.get(name='J.K. Rowling')
            books_by_author = Book.objects.filter(author=author)
            self.stdout.write("Books by J.K. Rowling:")
            for book in books_by_author:
                self.stdout.write(f"- {book.title}")

            # List all books in a library
            library = Library.objects.get(name='Central Library')
            books_in_library = library.books.all()
            self.stdout.write("\nBooks in Central Library:")
            for book in books_in_library:
                self.stdout.write(f"- {book.title}")

            # Retrieve the librarian for a library
            librarian = Librarian.objects.get(library__name='Central Library')
            self.stdout.write(f"\nLibrarian for Central Library: {librarian.name}")
        except Author.DoesNotExist:
            self.stdout.write("Error: Author 'J.K. Rowling' not found. Please ensure sample data is created.")
        except Library.DoesNotExist:
            self.stdout.write("Error: Library 'Central Library' not found. Please ensure sample data is created.")
        except Librarian.DoesNotExist:
            self.stdout.write("Error: Librarian for 'Central Library' not found. Please ensure sample data is created.")
