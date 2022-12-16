from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.LoginPageView.as_view(), name='login'),
    path('games/', views.GameListView.as_view(), name='games-list'),
    path('<slug:slug>', views.GameDetailView.as_view(), name='game-detail'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<slug:slug>', views.ProfileView.as_view(), name='profile-detail'),
    path('liked/<int:pk>', views.LikeView, name='liked'),
] 

