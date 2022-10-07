from django.db import models
from django.contrib.auth.models import User

# def create_acount():
#     url = 'https://hackathon.lsp.team/hk/v1/wallets/new'
#     headers = {'Authorization': 'Bearer example-auth-code'}
#     payload = {'name': 'Mark', email: 'mark@bearer.sh'}
#     response = requests.post(url, data=payload)


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
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} of {self.user.username}'
