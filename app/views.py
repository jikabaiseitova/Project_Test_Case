from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Author, Book
from .form import BookForm


menu = ["Авторы", "Книги"]


def index(request):
    books = Book.objects.all()
    context = {
        'menu': menu,
         'title': 'Добро пожаловать на наш сайт!',
         'book_form': BookForm()

    }
    return render(request, "index.html", context=context)


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'
    pk_url_kwarg = 'book_id'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse_lazy('book-list')

