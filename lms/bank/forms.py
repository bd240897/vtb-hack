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
    to_account = forms.CharField(label='', widget=forms.TextInput(attrs=to_account_attr),) # initial='0x15Cc4abzz27647ec9fE70D892E55586074263dF0'
    amount = forms.CharField(label='', widget=forms.TextInput(attrs=amount_id_attr), initial='1')


class TransferNFTForm(forms.Form):
    """Перевести для перевода денег"""
    to_account_attr = {"type": "text",
                       "class": "form-control",
                       "placeholder": "Кому перевести?", }

    token_id_attr = {"type": "text",
                     "class": "form-control",
                     "placeholder": "Номер NFT", }

    to_account = forms.CharField(label='', widget=forms.TextInput(attrs=to_account_attr)) # initial='0x15Cc4abzz27647ec9fE70D892E55586074263dF0'
    token_id = forms.CharField(label='', widget=forms.TextInput(attrs=token_id_attr)) # , initial='5'


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
        exclude = ('user', 'status')

        name_attrs = {"type": "text",
                      "class": "form-control",
                      "placeholder": "Ваше имя", }

        city_attrs = {"type": "text",
                      "class": "form-control",
                      "placeholder": "Ваш город", }

        rank_attrs = {"type": "text",
                      "class": "form-control",
                      "placeholder": "Ваша должность", }

        description_attrs = {"type": "text",
                             "class": "form-control",
                             "placeholder": "О себе",
                             "cols": '60',
                             "rows": "10"}

        widgets = {
            'name': forms.TextInput(attrs=name_attrs),
            'city': forms.TextInput(attrs=city_attrs),
            'rank': forms.TextInput(attrs=rank_attrs),
            'description': forms.Textarea(attrs=description_attrs),
        }


from django.contrib.auth.models import User


class CreateGroupForm(forms.Form):
    name = forms.CharField()
    owner = forms.ChoiceField(choices=[]) # , widget=forms.Select(attrs={"class": "form-select"})

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
