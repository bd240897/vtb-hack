from django.views.generic import TemplateView
from ..models import *


class TestView(TemplateView):
    template_name = 'bank/django_templates/index.html'


class MainView(TemplateView):
    template_name = 'bank/pages/main.html'


class ProfileView(TemplateView):
    template_name = 'bank/pages/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = Customer.objects.get(user=self.request.user)
        self.get_balance()
        context['balance'] = self.balance
        self.get_history_transaction()
        context['history'] = self.history
        return context

    def get_balance(self):
        account = Account.objects.get(user=self.request.user)
        publicKey = account.publicKey
        print(publicKey)
        url = f'https://hackathon.lsp.team/hk/v1/wallets/{publicKey}/balance'
        response = requests_lib.get(url)
        respons_json = response.json()
        print(respons_json)
        maticAmount = respons_json.get("maticAmount")
        coinsAmount = respons_json.get("coinsAmount")
        self.balance = {"maticAmount": maticAmount, "coinsAmount": coinsAmount}

    def get_history_transaction(self):
        account = Account.objects.get(user=self.request.user)
        publicKey = account.publicKey

        url = f'https://hackathon.lsp.team/hk/v1/wallets/{publicKey}/history'
        payload = {"page": 0, "offset": 100, "sort": "asc"}
        response = requests_lib.post(url, data=payload)
        respons_json = response.json()
        print(respons_json)
        self.history = respons_json

class ProfileEditView(TemplateView):
    template_name = 'bank/pages/profile_edit.html'


class PanelView(TemplateView):
    template_name = 'bank/pages/admin_panel.html'


class ShopView(TemplateView):
    template_name = 'bank/pages/shop.html'
