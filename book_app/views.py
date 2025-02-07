from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'book_app/index.html', context={
        'books': books,
    })
