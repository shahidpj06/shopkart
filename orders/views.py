from django.shortcuts import render, redirect
from . models import *
from products.models import *

def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    context = {
        'cart_obj': cart_obj
    }
    return render(request, 'cart.html', context)


def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        cart_obj, created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item, created = OrderItem.objects.get_or_create(
            owner = cart_obj,
            product = product,
        )
        if created: # if the cart is empty
            ordered_item.quantity = quantity
            ordered_item.save()
        else: # if the same item already exist in the cart it will add to the existing item  
            ordered_item.quantity += quantity
            ordered_item.save()
        return redirect('cart_details')
    

def remove_item(request, pk):
    item = OrderItem.objects.get(pk=pk)
    if item:
        item.delete()
    
    return redirect('cart_details')