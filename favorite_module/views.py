from django.contrib.auth.decorators import login_required
from cookie_project.settings import LOGIN_URL
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import View

from favorite_module.models import Favorite, FavoriteDetail
from order_module.views import add_to_cart
from product_module.models import Product


# Create your views here.
@method_decorator(login_required, name='dispatch')
class add_to_favorites(View):
    def get(self, request):
        product_id = request.GET.get('products_id')
        if request.user.is_authenticated:
            product = Product.objects.filter(pk=product_id, is_active=True).first()
            if product is not None:
                current_favorite, created = Favorite.objects.get_or_create(user=request.user)
                current_favorite_product = current_favorite.favoritedetail_set.filter(product_id=product_id).exists()
                if not current_favorite_product:
                    new_detail = FavoriteDetail(
                        favorite=current_favorite,
                        product=product,
                    )
                    new_detail.save()
                    return JsonResponse({
                        'status': 'success',
                        'text': 'محصول با موفقیت به لیست علاقه مندی ها اضافه شد',
                        'confirmButtonTextBack': 'باشه',
                        'icon': 'success'

                    })
                else:
                    return JsonResponse({
                        'status': 'error',
                        'text': 'محصول در لیست علاقه مندی های شما وجود دارد',
                        'confirmButtonTextBack': 'باشه',
                        'icon': 'info'
                    })

        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای اضافه کردنه محصول به سبد خرید میبایست اول وارد سایت شوید',
            'confirmButtonTextBack': 'لاگ این',
            'icon': 'info'
        })

@method_decorator(login_required, name='dispatch')
class Favorite_View(View):
    def get(self, request):
        current_favorite, created = Favorite.objects.prefetch_related('favoritedetail_set').get_or_create(
            user=request.user)

        context = {
            'favorites': current_favorite
        }
        return render(request, 'favorite_module/favorite_list.html', context)


@method_decorator(login_required, name='dispatch')
class remove_product_from_favorites(View):
    def get(self, request):
        product_id = request.GET.get('productId')
        if product_id is not None:
            product = Product.objects.filter(pk=product_id).first()
            num, current_product_favorite = FavoriteDetail.objects.filter(
                id=product_id,
                favorite__user_id=self.request.user.id
            ).first().delete()
            if num == 0:
                return JsonResponse({
                    'status': 'product_not_found',
                })
            current_favorite, created = Favorite.objects.prefetch_related('favoritedetail_set').get_or_create(
                user=request.user)

            context = {
                'favorites': current_favorite
            }

            return JsonResponse({
                'status': 'success',
                'data': render_to_string('favorite_partial/success_favorite_rm.html', context)

            })
        return JsonResponse({
            'status': 'error'
        })
