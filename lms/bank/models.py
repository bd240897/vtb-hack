from django.db import models
from django.contrib.auth.models import User
import requests as requests_lib

class Profile(models.Model):
    """Дополнительные данные для профиля юзера"""

    name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='bank/profile', default='bank/profile/avatar_default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = {
        ('user', 'user'),
        ('admin', 'admin'),
        ('editor', 'editor'),
        ('boss', 'boss'),
    }

    status = models.CharField(verbose_name="Статус ", max_length=32, default="user", blank=True, choices=CHOICES)

    def is_user_admin(self):
        pass

    def is_user_editor(self):
        pass

    def is_user_boss(self):
        pass


    def __str__(self):
        return f'{self.id} of {self.user.username}'

# TODo mayby rename to wallet?
class Account(models.Model):
    """Аккаунт с данными для кошелька"""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    publicKey = models.CharField(max_length=255, blank=True, null=True)
    privateKey = models.CharField(max_length=255, blank=True, null=True)

    def create_wallet(self):
        url = 'https://hackathon.lsp.team/hk/v1/wallets/new'
        response = requests_lib.post(url)
        respons_json = response.json()
        publicKey = respons_json.get("publicKey")
        privateKey = respons_json.get("privateKey")
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.save()

    def __str__(self):
        return f'{self.id} of {self.user.username}'


class VtbGroup(models.Model):
    """Группы"""

    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_onwer')
    users = models.ManyToManyField(User, related_name='group_users')



