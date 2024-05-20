from django.urls import path
from . import views

urlpatterns = [
    path('cart_details/', views.show_cart, name='cart_details')
]