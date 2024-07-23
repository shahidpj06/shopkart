from django.shortcuts import render, get_object_or_404
from . models import Product
from django.core.paginator import Paginator
from django.db.models import Q

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
    page = request.GET.get('page', 1)
    sort_option = request.GET.get('sort', 'priority')

    if sort_option == 'low_price':
        products_list = Product.objects.order_by('price')
    elif sort_option == 'high_price':
        products_list = Product.objects.order_by('-price')
    elif sort_option == 'newest':
        products_list = Product.objects.order_by('-created_at')
    else:
        products_list = Product.objects.order_by('priority')

    products_paginator = Paginator(products_list, 12)
    products_list = products_paginator.get_page(page)

    context = {
        'products': products_list,
        'sort': sort_option
    }
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


def search_product(request):
    if request.method == 'POST':
        search_bar = request.POST.get('search')
        products = Product.objects.filter(Q(title__contains=search_bar) | Q(brand__contains=search_bar))
        result_count = products.count()
        context = {
            'products': products,
            'search_bar': search_bar,
            'result_count': result_count
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
    

def product_sorting(request):
    sort_option = request.GET.get('sort', 'default')

    if sort_option == 'low_price':
        products = Product.objects.all().order_by('price')
    elif sort_option == 'high_price':
        products = Product.objects.all().order_by('-price')
    elif sort_option == 'newest':
        products = Product.objects.all().order_by('-created_at')
    else:
        products = Product.objects.all()

    return render(request, 'products.html', {'products': products})
