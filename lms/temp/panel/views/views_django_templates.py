from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, RedirectView, CreateView
from ..models import *
from ..forms import *
from django.contrib import messages

########### ИМПОРТЫ ИЗ BANK ####################
from bank.logic import *
from bank.models import *

class PanelAdminView(TemplateView):
    template_name = 'panel/admin.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    """Профиль пользователя"""

    template_name = 'bank/pages/profile.html'
    login_url = 'game_login'
    redirect_field_name = 'main'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            messages.error(request, "У админа нет профиля!")
            return HttpResponseRedirect(reverse("main"))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # данные профиля
        profile = Profile.objects.get(user=self.request.user)
        id_profile = profile.id
        context['profile'] = profile
        context['id_profile'] = id_profile

        # данные акканута
        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        private_key = account.privateKey

        # TODO delete ot
        # данные для отладки
        context['public_key'] = public_key
        context['private_key'] = private_key

        # получение баланса и истории транзакций
        context['balance'] = get_balance(public_key=public_key)
        context['balance_NFT'] = get_balance_NFT(public_key=public_key)
        context['history'] = get_history_transaction(public_key=public_key).get('history')[:10]

        # форма перевода денег
        context['form'] = TransferCoinForm()
        context['form_NFT'] = TransferNFTForm()
        context['form_generate_NFT'] = GenerateNFTForm()
        return context

    def post(self, request, *args, **kwargs):
        # работа с формой для перевода денег

        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        private_key = account.privateKey

        to_public_key = request.POST.get('to_account')
        amount = request.POST.get('amount')
        type_coin = request.POST.get('type_coin')

        if type_coin == 'matic':
            response = transfer_rubles(from_private_key=private_key, to_public_key=to_public_key, amount=amount)
            messages.success(request, response)
        elif type_coin == 'ruble':
            response = transfer_matic(from_private_key=private_key, to_public_key=to_public_key, amount=amount)
            messages.success(request, response)
        return super().get(self, request, *args, **kwargs)

