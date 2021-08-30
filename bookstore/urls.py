from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', views.all_books, name = 'all_books'),
    path('item/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list')
]

