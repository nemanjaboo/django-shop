from django.shortcuts import get_object_or_404, render

from .models import Books, Category

# if we are not using default templates folder app/templates/app we need to add our custom templates folder in settings.py,
# TEMPLATES, DIRS


def all_books(request):
    books = Books.booksm.all()  # books.products - new model manager in models.py
    return render(request, 'bookstore/home.html', {'books':books})

def book_detail(request, slug):
    book = get_object_or_404(Books, slug = slug, in_stock=True)
    return render(request, 'bookstore/book_detail.html', {'book':book})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = Books.objects.filter(category=category)
    #with selected query above defined we can use that query to filter all Book objects
    return render(request, 'bookstore/category.html', {'category':category, 'books':books})
