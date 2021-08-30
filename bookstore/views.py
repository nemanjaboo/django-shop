from django.shortcuts import render, get_object_or_404
from .models import Category, Books

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_books(request):
    books = Books.objects.all()
    return render(request, 'bookstore/home.html', {'books':books})

def book_detail(request, slug):
    book = get_object_or_404(Books, slug = slug, in_stock=True)
    return render(request, 'bookstore/book_detail.html', {'book':book})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = Books.objects.filter(category=category)
    return render(request, 'bookstore/category.html', {'category':category, 'books':books})