from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('<slug:slug>', views.GameDetailView.as_view(), name='game-detail'),
    path('', views.GameListView.as_view(), name='games-list'),
    
] 

