from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from ..models import *
from ..forms import *
from django.contrib import messages

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
        context['form'] = TransferForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TransferForm(request.POST)
        from_account = request.POST.get('from_account')
        to_account = request.POST.get('to_account')
        amount = request.POST.get('amount')
        type_coin = request.POST.get('type_coin')
        if type_coin == 'matic':
            response = self.transfer_rubles(from_account, to_account, amount)
            messages.success(request, response)
        elif type_coin == 'ruble':
            messages.error(request, "Метод еще не реализован!!!")
        elif type_coin == 'nft':
            messages.error(request, "Метод еще не реализован!!!")
        return super().get(self, request, *args, **kwargs)

    def transfer_rubles(self, fromPrivateKey, toPublicKey, amount):
        account = Account.objects.get(user=self.request.user)
        publicKey = account.publicKey

        url = f'https://hackathon.lsp.team/hk/v1/transfers/ruble'
        payload = {
            "fromPrivateKey": fromPrivateKey,
            "toPublicKey": toPublicKey,
            "amount": amount
            }
        response = requests_lib.post(url, data=payload)
        respons_json = response.json()
        print(respons_json)
        return respons_json

    def transfer_matic(self):
        pass

    def transfer_NFT(self):
        pass

    def get_balance(self):
        account = Account.objects.get(user=self.request.user)
        publicKey = account.publicKey

        url = f'https://hackathon.lsp.team/hk/v1/wallets/{publicKey}/balance'
        response = requests_lib.get(url)
        respons_json = response.json()
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
        self.history = respons_json


class ProfileEditView(UpdateView):
    template_name = 'bank/pages/profile_edit.html'
    form_class = ProfleEditForm
    queryset = Customer.objects.all()

    def get_success_url(self):
        return reverse('profile')

class PanelView(TemplateView):
    template_name = 'bank/pages/admin_panel.html'


class ShopView(TemplateView):
    template_name = 'bank/pages/shop.html'
