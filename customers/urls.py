from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('account_details/', views.show_account, name='account_details'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('logout/', views.sign_out, name='logout')
]