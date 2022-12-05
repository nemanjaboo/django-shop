import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()
from shop.models import Game
from scraper import final_games_dict

for i in range(len(final_games_dict.keys())):
    game = final_games_dict.get(i)
    try:
        game_obj = Game.objects.get(name=game['title'])
        if game_obj:
            game_obj.price = game['price']
            game_obj.status = game['status']
            game_obj.save()
    except Game.DoesNotExist:
        game = Game(name=game['title'], price=game['price'], status=game['status'], image=game['image'])
        game.save()
