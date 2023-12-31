from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DeleteView


class BookListView(ListView):
    model = Book 
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DeleteView):
    model = Book 
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


