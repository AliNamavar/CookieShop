from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from favorite_module.models import Favorite, FavoriteDetail
from product_module.models import Product


# Create your views here.

class add_to_favorites(View):
    def get(self, request):
        product_id = request.GET.get('products_id')
        if request.user.is_authenticated:
            product = Product.objects.filter(pk=product_id, is_active=True).first()
            if product is not None:
                current_favorite, created = Favorite.objects.get_or_create(user=request.user)
                current_favorite_product = current_favorite.favoritedetail_set.filter(pk=product_id).first()
                if current_favorite_product is None:
                    new_detail = FavoriteDetail(
                        favorite=current_favorite,
                        product=product,
                    )
                    new_detail.save()
                    return JsonResponse({
                        'status': 'success',
                        'text': 'محصول با موفقیت به سبد خرید شما اضافه شد',
                        'confirmButtonTextBack': 'باشه',
                        'icon': 'success'

                    })
                return JsonResponse({
                    'status': '404',
                    'text': 'محصول مورد نظر یافت نشد',
                    'confirmButtonTextBack': 'باشه',
                    'icon': 'error'

                })

        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای اضافه کردنه محصول به سبد خرید میبایست اول وارد سایت شوید',
            'confirmButtonTextBack': 'لاگ این',
            'icon': 'info'
        })


class Favorite_View(View):
    def get(self, request):
        current_favorite, created = Favorite.objects.prefetch_related('favoritedetail_set').get_or_create(user=request.user)

        context = {
            'favorites': current_favorite
        }
        return render(request, 'favorite_module/favorite_list.html', context)

