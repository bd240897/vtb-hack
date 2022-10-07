from django.db import models
from django.contrib.auth.models import User
import requests as requests_lib



class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to='bank/customer')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
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
