from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView, DetailView, RedirectView
from ..forms import *
from ..models import Account
from django.contrib.auth.models import User

# //////////////////////////// LOGIN ////////////////////////////////////////


class RegisterUser(CreateView):
    """Регистрация"""

    form_class = RegisterUserForm
    template_name = 'bank/login/register.html'
    success_url = reverse_lazy('game_login')

    def form_valid(self, form):
        user = form.save()
        account = Account.objects.create(user=user)
        account.create_wallet()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect('profile')

class LoginUser(LoginView):
    """Логин"""

    form_class = LoginUserForm
    template_name = 'bank/login/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class TempView(TemplateView):
    """Заглушка"""

    template_name = 'bank/login/home.html'


def logout_user(request):
    """Разлогиниться"""

    logout(request)
    return redirect('main')