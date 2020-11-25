from django.contrib.auth.mixins import (
    LoginRequiredMixin, # limits access to the Books pages only to logged-in users
    PermissionRequiredMixin # basic permissions system that is controlled through the Django admin
)
from django.db.models import Q # new
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list' # default value = object_list
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status' # to review the detail page user must have a permission


class SearchResultsListView(ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
