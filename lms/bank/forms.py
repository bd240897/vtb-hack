from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterUserForm(UserCreationForm):
    """Форма регитсрации"""

    parm_username = {"type": "text",
                     "class": "form-control",
                     "placeholder": "Ваше имя", }

    param_password1 = {"type": "text",
                       "class": "form-control",
                       "placeholder": "Ваш пароль", }

    param_password2 = {"type": "text",
                       "class": "form-control",
                       "placeholder": "Повторите пароль", }

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs=parm_username))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=param_password1))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs=param_password2))

    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-input'}),
    #         'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
    #         'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
    #         'email': forms.EmailInput(attrs={'class': 'form-input'}),
    #     }


class LoginUserForm(AuthenticationForm):
    """Форма логина"""

    parm_username = {"type": "text",
                     "class": "form-control",
                     "placeholder": "Ваше имя", }

    param_password = {"type": "text",
                      "class": "form-control",
                      "placeholder": "Ваш пароль", }

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs=parm_username))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=param_password))

    # class Meta:
    #     parm_username = {"type": "text",
    #                      "class": "form-control",
    #                      "placeholder": "Напишите Ваше сообщение", }
    #
    #     param_password = {"type": "text",
    #                       "class": "form-control",
    #                       "placeholder": "Напишите номер раунда", }
    #
    #     fields = ('username', 'password')
    #
    #     widgets = {
    #         'username': forms.TextInput(attrs=parm_username),
    #         'password': forms.PasswordInput(attrs=param_password),
    #     }

class TransferForm(forms.Form):
    """Перевести бабло"""
    CHOICES = (
        ('matic', 'matic'),
        ('ruble', 'ruble'),
        ('nft', 'nft'),
    )
    type_coin = forms.ChoiceField(widget=forms.Select, choices=CHOICES, initial='matic')
    from_account = forms.CharField(label='', widget=forms.TextInput(), initial='1cc9bfcb74505f68521d03b7379cb1e92fe12cdc4717f709b517250ca0f9fc44')
    to_account = forms.CharField(label='', widget=forms.TextInput(), initial='0x15Cc4abzz27647ec9fE70D892E55586074263dF0')
    amount = forms.CharField(label='', widget=forms.TextInput(), initial='1')

class ProfleEditForm(forms.ModelForm):
    """"""

    class Meta:
        model = Customer
        fields = "__all__"

