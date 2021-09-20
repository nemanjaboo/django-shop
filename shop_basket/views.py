from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .basket import Basket
from bookstore.models import Books
from django.http import JsonResponse

def basket_summary(request):
    return render(request, 'bookstore/basket/basket.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post': # checking if request from Ajax is post request and if action equals post like in ajax script
        book_id = int(request.POST.get('booksid'))# id field in Ajax script
        book = get_object_or_404(Books, id=book_id)
        basket.add(book=book)
        response = JsonResponse({'test':'data'})
        return response