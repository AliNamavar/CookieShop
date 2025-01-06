from django import template

register = template.Library()

@register.filter
def custom_range(value):
    return range(value)



@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + 'تومان'


@register.simple_tag
def multiply(value, arg):
    return value * arg