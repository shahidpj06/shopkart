from django.urls import path
from . import views

urlpatterns = [
    path('account_details/', views.show_account, name='account_details')
]