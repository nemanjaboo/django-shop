from django.contrib import admin
from shop.models import Game, Category, Favorite, Profile

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Favorite, FavoriteAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)