from django.urls import path

from .views import index, AuthorList, BookList, BookDetail, BookCreateView


urlpatterns = [
    path('', index),
    path('author/', AuthorList.as_view()),
    path('book/', BookList.as_view(), name='book-list'),
    path('book/<int:book_id>/', BookDetail.as_view(), name='detail'),
    path('book/create/', BookCreateView.as_view(), name='create_book'),
]
