from django.db import models
from customers.models import Customer
from products.models import Product

# model for ordering the items with there status
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, "Live"), (DELETE, "Delete"))

    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = (
        (ORDER_PROCESSED, 'ORDER_PROCESSED'),
        (ORDER_DELIVERED, 'ORDER_DELIVERED'),
        (ORDER_CONFIRMED, 'ORDER_CONFIRMED')
    )

    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True)
    total_price = models.FloatField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "order-{}-{}".format(self.id, self.owner.user.username)


# model for ordered items with quantity and product. Each cart has multiple items
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="order_items", null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items') # Each order has multiple orderitems
