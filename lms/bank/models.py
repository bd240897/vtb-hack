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
