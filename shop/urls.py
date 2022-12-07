from django.urls import path
from . import views 

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.GameDetailView.as_view(), name='game-detail'),
    path('games/', views.GameListView.as_view(), name='games-list')
] 

