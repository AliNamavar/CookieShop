import json
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from order_module.models import Order, OrderDetail
from product_module.models import Product
from .models import Order

# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

# amount = 1000
description = "نهایی کردنه خرید شما"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
CallbackURL = 'http://127.0.0.1:8080/verify-payment/'


def request_payment(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": Order.calculate_total,
        "Description": description,
        # "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                        'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify_payment(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": Order.calculate_total,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response


@login_required
def add_to_cart(request):
    product_id = request.GET.get('product_id')
    count = int(request.GET.get('count'))

    if request.user.is_authenticated:
        product = Product.objects.filter(pk=product_id, is_active=True).first()
        if count < product.number:
            return JsonResponse({
                'status': 'count_prob',
                'text': 'مقدار وارد شده صحیح نیست ',
                'confirmButtonTextBack': 'باشه',
                'icon': 'error'

            })
        if product is not None:
            current_cart, created = Order.objects.get_or_create(is_paid=False, user=request.user)
            current_cart_product = current_cart.orderdetail_set.filter(product_id=product_id).first()

            if current_cart_product is not None:
                current_cart_product.count += int(count)
                current_cart_product.save()
            else:
                new_detail = OrderDetail(
                    order_id=current_cart.id,
                    product_id=product_id,
                    count=count,
                )
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول با موفقیت به سبد خرید شما اضافه شد',
                'confirmButtonTextBack': 'باشه',
                'icon': 'success',
                'cart_total_price': current_cart.calculate_total()
            })
        else:
            return JsonResponse({
                'status': '404',
                'text': 'محصول مورد نظر یافت نشد',
                'confirmButtonTextBack': 'باشه',
                'icon': 'error'

            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای اضافه کردنه محصول به سبد خرید میبایست اول وارد سایت شوید',
            'confirmButtonTextBack': 'لاگ این',
            'icon': 'info'
        })


@login_required
def cart_view(request):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user=request.user)
    total_price = current_order.calculate_total()

    context = {
        'order': current_order,
        'total_price': total_price,
    }

    return render(request, 'order_module/cart_list.html', context)

@login_required
def remove_order_detail(request):
    product_id = request.GET.get('product_rm_id')
    if product_id is None:
        return JsonResponse({
            'status': 'id_not_found',
        })

    num, deleted_dict = OrderDetail.objects.filter(pk=product_id, order__user_id=request.user.id,
                                                   order__is_paid=False).delete()
    if num == 0:
        return JsonResponse({
            'status': 'product_not_found',
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user=request.user)

    total_price = current_order.calculate_total()

    context = {
        'order': current_order,
        'total_price': total_price,
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('cart_partials/cart_list_partials.html', context),
        'cart_total_price': current_order.calculate_total()


    })


@login_required
def update_cart_product_count(request):
    product_id = request.GET.get('product_id_count_edit')
    try:
        count = int(request.GET.get('new_count'))
    except (TypeError, ValueError):
        return JsonResponse({
            'status': 'id_not_found',
            'message': 'Invalid product ID or count',
            # 'cart_total_price': current_cart.calculate_total()

        })

    current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)
    detail = OrderDetail.objects.filter(pk=product_id, order__user_id=request.user.id,
                                                   order__is_paid=False).first()

    if detail is None:
        return JsonResponse({
            'status': 'error',
            'message': 'Product not found in cart'
        })

    if count < 1 or count < detail.product.number:
        return JsonResponse({
            'status': 'error',
            'message': 'مقدار وارد شده صحیح نیست'
        })

    detail.count = count
    detail.save()


    context = {
        'order': current_order,
        'total_price': current_order.calculate_total,
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('cart_partials/cart_list_partials.html', context),
        'cart_total_price': current_order.calculate_total()

    })
