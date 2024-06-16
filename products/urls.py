from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list/', views.list_products, name='list_products'),
    path('product_details/<pk>', views.product_details, name='product_details'),
    # path('offer_product/', views.offer_product, name="offer_product")
]