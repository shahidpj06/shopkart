from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views import View, generic
from django.contrib import messages
from customers.forms import EditProfileForm
from . models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin


def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            )

            customer = Customer.objects.create(
                name = username,
                user = user,
                address = address,                                 
                phone = phone
            )
            success_message = "User registered successfully"
            messages.success(request, success_message)
        except Exception as e:
            error_message = "Invalid username or password inputs"
            messages.error(request, error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
            messages.error(request, error_message)

    return render(request, 'account.html', context)


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def sign_out(request):
    logout(request)
    return redirect('home')