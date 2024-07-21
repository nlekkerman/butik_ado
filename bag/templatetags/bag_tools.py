from decimal import Decimal
from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    try:
        subtotal = Decimal(price) * int(quantity)
    except (ValueError, TypeError):
        subtotal = Decimal('0.00')  # Handle invalid input gracefully
    return subtotal
