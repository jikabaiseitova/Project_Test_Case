from django.test import TestCase
from .models import Author, Book
from django.urls import reverse


class BookTestCase(TestCase):
    def setUp(self):
        author = Author.objects.create(name="John Doe")
        Book.objects.create(title="Book 1", author=author, publication_date="2023-01-01")
        Book.objects.create(title="Book 2", author=author, publication_date="2023-02-01")

    def test_select_related(self):
        book = Book.objects.select_related('author').get(title="Book 1")
        self.assertEqual(book.author.name, "John Doe")

    def test_prefetch_related(self):
        author = Author.objects.prefetch_related('book_set').get(name="John Doe")
        books = author.book_set.all()
        self.assertEqual(len(books), 2)


class AuthorListViewTestCase(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Jane Smith")
        Book.objects.create(title="Book 3", author=author, publication_date="2023-03-01")
        Book.objects.create(title="Book 4", author=author, publication_date="2023-04-01")

    def test_author_list_view(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Smith")
        self.assertContains(response, "Book 3")
        self.assertContains(response, "Book 4")
