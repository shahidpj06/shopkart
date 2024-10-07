from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from . models import Customer
from django import forms


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    address = forms.Textarea()
    phone = forms.IntegerField()

    class Meta:
        model = Customer
        fields = ('username', 'email', 'address', 'phone')