from django.urls import path
from .views import book, author, author_detail, HomeView, search, autocomplete, book_update, book_delete, \
    book_update_done, book_delete_done, add_book, BookView, pro_search, pro_search_done, favorite, favorite_page

urlpatterns = [
    # path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('books/<title>', BookView.as_view(), name='book'),
    path('add-book', add_book, name='add-book'),
    path('pro-search', pro_search, name='pro-search'),
    path('pro-search-done', pro_search_done, name='pro-search-done'),
    path('authors', author, name='authors'),
    path('detail/<name>', author_detail, name='author-detail'),
    # path('books/<title>', book, name='book'),
    path('book-update', book_update, name='book-update'),
    path('favorite', favorite, name='favorite'),
    path('favorite-page', favorite_page, name='favorite-page'),
    path('book-update-done', book_update_done, name='book-update-done'),
    path('book-delete', book_delete, name='book-delete'),
    path('book-delete_done', book_delete_done, name='book-delete_done'),
    path('search', search),
    path('autocomplete-search/', autocomplete, name='autocomplete-search'),
]
