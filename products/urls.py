from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list/', views.list_products, name='list_products'),
    path('product_details/<pk>', views.product_details, name='product_details'),
    path('search_product/', views.search_product, name='search_product'),
]