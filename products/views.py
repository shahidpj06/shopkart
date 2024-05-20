from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def list_products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    products_list = Product.objects.all()
    products_paginator = Paginator(products_list, 12)
    products_list = products_paginator.get_page(page)
    context = {'products': products_list}
    return render(request, 'products.html', context)

def product_details(request):
    return render(request, 'product_details.html')