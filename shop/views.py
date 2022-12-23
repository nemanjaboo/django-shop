from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import View
from .forms import SignUpForm, LoginForm
from .models import Game, Profile, Favorite

def index(request):
    return HttpResponse("Hello, world. You are at the shop")

def logout_view(request):
    logout(request)
    return redirect('shop:login')

def LikeView(request, pk):
    game = get_object_or_404(Game, id=request.POST.get('game_id'))
    profile = Profile.objects.get(user=request.user.id)
    if game not in profile.favorites.all():
        favorite = Favorite.objects.create()
        favorite.profile.add(profile)
        favorite.game.add(game)
        profile.favorites.add(game)
        favorite.save()
        return redirect('shop:games-list')
    else:
        fav = Favorite.objects.get(profile=profile, game=game)
        profile.favorites.remove(game)
        fav.delete()
        return redirect('shop:games-list')


class GameDetailView(DetailView):
    model = Game
    template_name: 'game_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_name = context['game']
        game = get_object_or_404(Game, name=game_name)
        profile = Profile.objects.get(user=self.request.user.id)
        if game in profile.favorites.all():
            context.update({
                'game_faved': True
            })
        return context
       
class GameListView(ListView):
    model = Game
    template_name = 'game_list'
    paginate_by =  5
    ordering = ['name']
  

    def post(self, request, *args, **kwargs):
        # mylist = request.POST.getlist('sorting')
        self.ordering = request.POST.getlist('sorting')
        return super(GameListView, self).get(request, *args, **kwargs)
    

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('shop:games-list')
    template_name = 'shop/signup.html'


class LoginPageView(View):
    template_name = 'shop/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form':form, 'message': message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('shop:games-list')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

class ProfileView(DetailView):
    model = Profile
    template_name = 'shop/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user.id)
        context['fav_games'] = profile.favorites.all()
        return context

class SearchView(ListView):
    model = Game
    context_object_name = 'games'
    template_name ='shop/search_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(name__contains=query.upper())
