from django import template
from .get_total import get_total

register = template.Library()

@register.simple_tag(name='final_amount')
def final_amount(amount):
    gst_amount = 18
    net_price = get_total(amount)
    applied_amount = net_price * gst_amount / 100
    total_price = applied_amount + net_price
    return total_price