from django.shortcuts import render, get_object_or_404
from . models import Product
from django.core.paginator import Paginator

def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    offer_product = get_object_or_404(Product, pk=24)
    offer_product_image = offer_product.images.first()
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
        'offer_product': offer_product,
        'offer_product_image': offer_product_image
    }
    return render(request, 'index.html', context)

def list_products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    products_list = Product.objects.order_by('priority')
    products_paginator = Paginator(products_list, 12)
    products_list = products_paginator.get_page(page)
    context = {'products': products_list}
    return render(request, 'products.html', context)

def product_details(request, pk):
    featured_products = Product.objects.order_by('priority')[:4]
    product = get_object_or_404(Product, pk=pk)
    product_images = product.images.all()
    context = {
        'featured_products': featured_products,
        'product': product,
        'product_images': product_images
    }
    return render(request, 'product_details.html', context)
