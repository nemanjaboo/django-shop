from django.urls import path

from . import views

app_name = 'bookstore'
# app_name is matching the namespace from shop/urls.py
# it is useful because we can later refer to these urls through it's app_name

urlpatterns = [
    path('', views.all_books, name = 'all_books'),
    path('<slug:slug>', views.book_detail, name='book_detail'),
    # first slug is data type, second slug is going to be the actual slug
    path('shop/<slug:category_slug>/', views.category_list, name='category_list')
]

