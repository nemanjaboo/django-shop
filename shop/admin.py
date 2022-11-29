from django.contrib import admin
from shop.models import Game, Category

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)