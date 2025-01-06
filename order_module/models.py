from django.db import models
from account_module.models import User
from product_module.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='برداخت شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ برداخت')

    def __str__(self):
        return self.user.get_full_name()

    def calculate_total(self):
        total_price = 0
        if self.is_paid:
            for product_detail in self.orderdetail_set.all():
                total_price += product_detail.final_price * product_detail.count

        else:
            for product_detail in self.orderdetail_set.all():
                total_price += product_detail.product.price * product_detail.count

        return total_price


    class Meta:
        verbose_name = 'shop cart'
        verbose_name_plural = 'Users shop carts'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')


    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'cart shop detail'
        verbose_name_plural = 'cart shop details list'