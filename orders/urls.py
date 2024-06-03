from django.urls import path
from . import views

urlpatterns = [
    path('cart_details/', views.show_cart, name='cart_details'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart')
]