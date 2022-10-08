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


class TransferCoinForm(forms.Form):
    """Перевести для перевода денег"""

    CHOICES = (
        ('matic', 'matic'),
        ('ruble', 'ruble'),
    )
    type_coin = {"class": "form-select"}

    to_account_attr = {"type": "text",
                       "class": "form-control",
                       "placeholder": "Кому перевести?", }

    amount_id_attr = {"type": "text",
                      "class": "form-control",
                      "placeholder": "Количество", }

    type_coin = forms.ChoiceField(widget=forms.Select(attrs=type_coin), choices=CHOICES, initial='matic')
    to_account = forms.CharField(label='', widget=forms.TextInput(attrs=to_account_attr),
                                 initial='0x15Cc4abzz27647ec9fE70D892E55586074263dF0')
    amount = forms.CharField(label='', widget=forms.TextInput(attrs=amount_id_attr), initial='1')


class TransferNFTForm(forms.Form):
    """Перевести для перевода денег"""
    to_account_attr = {"type": "text",
                       "class": "form-control",
                       "placeholder": "Кому перевести?", }

    token_id_attr = {"type": "text",
                     "class": "form-control",
                     "placeholder": "Номер NFT", }

    to_account = forms.CharField(label='', widget=forms.TextInput(attrs=to_account_attr),
                                 initial='0x15Cc4abzz27647ec9fE70D892E55586074263dF0')
    token_id = forms.CharField(label='', widget=forms.TextInput(attrs=token_id_attr), initial='5')

class GenerateNFTForm(forms.Form):
    """Перевести для перевода денег"""
    amount_attr = {"type": "text",
                   "class": "form-control",
                   "placeholder": "Количество NFT", }

    amount = forms.CharField(label='Введите', widget=forms.TextInput(attrs=amount_attr))


class ProfleEditForm(forms.ModelForm):
    """Форма редактора профиля"""

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ('user',)



# lass
# CreateGroupForm(forms.ModelForm):
# """Форма редактора профиля"""
# owner = forms.ChoiceField(choices=[])
#
#
# class Meta:
#     name_attrs = {"type": "text",
#                   "class": "form-control text-center",
#                   "placeholder": "Название группы", }
#
#     model = VtbGroup
#     fields = ('name', 'owner')
#     widgets = {
#         'name': forms.TextInput(attrs=name_attrs)
#     }
#
#
# # def clean_owner(self):
# #     data = self.cleaned_data['owner']
# #     self.cleaned_data['owner'] = User.objects.get(id=self.cleaned_data['owner'])
# #     return data
#
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.fields['owner'].choices = [(User.objects.get(pk=x.id), x.username) for x in User.objects.all()]
#
#

from django.contrib.auth.models import User
class CreateGroupForm(forms.Form):
    name = forms.CharField()
    owner = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].choices = [(x.pk, x.username) for x in User.objects.all()]


class AddUserToGroupForm(forms.Form):
    user = forms.ChoiceField(choices=[])
    group = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].choices = [(x.pk, x.username) for x in User.objects.all()]
        self.fields['group'].choices = [(x.pk, x.name) for x in VtbGroup.objects.all()]







