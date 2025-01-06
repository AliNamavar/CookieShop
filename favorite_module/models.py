from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = 'user_favorite'
        verbose_name_plural = 'user_favorites'


class FavoriteDetail(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.favorite)

    class Meta:
        verbose_name = 'favorite_detail'
        verbose_name_plural = 'favorite_details'