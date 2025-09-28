from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from api.models import Author, Book

class BookAPIViewTests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    def setUp(self):
        """
        Set up a test environment with an author, books, and users.
        """
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username='adminuser',
            password='adminpassword',
            email='admin@test.com'
        )
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        self.book1 = Book.objects.create(
            title='The Hobbit',
            publication_year=1937,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title='The Lord of the Rings',
            publication_year=1954,
            author=self.author
        )

    # --- CRUD Tests ---

    def test_list_books(self):
        """
        Ensure we can retrieve a list of books.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_create_book(self):
        """
        Ensure we can create a new book as an authenticated user.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'The Silmarillion',
            'publication_year': 1977,
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='The Silmarillion').publication_year, 1977)

    def test_update_book(self):
        """
        Ensure we can update an existing book as an authenticated user.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'The Fellowship of the Ring',
            'publication_year': 1954,
            'author': self.author.id
        }
        response = self.client.put(f'/api/books/update/{self.book2.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.title, 'The Fellowship of the Ring')

    def test_delete_book(self):
        """
        Ensure we can delete a book as an admin user.
        """
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        
    # --- Functionality Tests (Filtering, Searching, Ordering) ---

    def test_filtering_books_by_year(self):
        """
        Ensure we can filter books by publication year.
        """
        response = self.client.get('/api/books/', {'publication_year': 1937})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_searching_books_by_title(self):
        """
        Ensure we can search for books by title.
        """
        response = self.client.get('/api/books/', {'search': 'hobbit'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_ordering_books_by_year(self):
        """
        Ensure we can order books by publication year.
        """
        response = self.client.get('/api/books/', {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')
        
    # --- Permissions Tests ---
    
    def test_unauthenticated_create_book_fails(self):
        """
        Ensure an unauthenticated user cannot create a book.
        """
        response = self.client.post('/api/books/create/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_unauthenticated_delete_book_fails(self):
        """
        Ensure an unauthenticated user cannot delete a book.
        """
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
