from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Game

def index(request):
    return HttpResponse("Hello, world. You are at the shop")

# Create your views here.

class GameDetailView(DetailView):
    model = Game
    template_name: 'game_detail'

class GameListView(ListView):
    model = Game
    template_name = 'game_list'
    paginate_by =  5
    ordering = ['name']
  

    def post(self, request, *args, **kwargs):
        # mylist = request.POST.getlist('sorting')
        self.ordering = request.POST.getlist('sorting')
        return super(GameListView, self).get(request, *args, **kwargs)


   