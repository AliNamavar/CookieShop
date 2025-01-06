from django.contrib import admin

from favorite_module.models import Favorite, FavoriteDetail

# Register your models here.
admin.site.register(Favorite)
admin.site.register(FavoriteDetail)
