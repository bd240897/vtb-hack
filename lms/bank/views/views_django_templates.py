from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, RedirectView, CreateView

from ..mixins.panel_admin_mixins import *
from ..models import *
from ..forms import *
from django.contrib import messages
from ..logic import *

class RedirectMainView(RedirectView):
    """Простой редирект на главную"""

    # https://ustimov.org/posts/11/
    def get_redirect_url(self):
        return reverse('main')

# class TestView(TemplateView):
#     template_name = 'bank/django_templates/index.html'

class MainView(TemplateView):
    """Главная страница"""

    template_name = 'bank/pages/main.html'


class ProfileView(PanelAdminMixi, LoginRequiredMixin, TemplateView):
    """Профиль пользователя"""

    template_name = 'bank/pages/profile.html'
    login_url = 'game_login'
    redirect_field_name = 'main'

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
        context['form_coin'] = TransferCoinForm()
        context['form_NFT'] = TransferNFTForm()
        context['form_generate_NFT'] = GenerateNFTForm()
        return context

class ProfileEditView(PanelAdminMixi, UpdateView):
    """Редактирование профиля"""

    # https://stackoverflow.com/questions/52263711/generic-view-updateview-from-django-tutorial-does-not-save-files-or-images
    template_name = 'bank/pages/profile_edit.html'
    form_class = ProfleEditForm
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse('profile')

class ActivitiesView(PanelAdminMixi, TemplateView):
    """Страница активностей"""

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse("profile"))
        return super().get(self, request, *args, **kwargs)

    template_name = 'bank/pages/activities.html'

class ShopView(PanelAdminMixi, TemplateView):
    """Страница магазина"""

    template_name = 'bank/pages/shop.html'


class GenerateNFTView(View):
    """Генерация NFT"""

    def post(self, request):

        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        private_key = account.privateKey

        form = GenerateNFTForm(request.POST)
        if form.is_valid():
            amount = request.POST.get('amount')
            response = generate_NFT(public_key, amount)
            messages.success(request, response)
            return HttpResponseRedirect(reverse("profile"))
        else:
            messages.error(request, 'Ошибка заполнения формы')
            return HttpResponseRedirect(reverse("profile"))

class TransferCoinView(View):
    """Перевод coin"""

    def post(self, request, *args, **kwargs):
        # работа с формой для перевода денег

        form = TransferCoinForm(request.POST)
        print(request.POST)
        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        private_key = account.privateKey

        if form.is_valid():
            to_public_key = request.POST.get('to_account')
            amount = form.cleaned_data.get('amount')
            type_coin = form.cleaned_data.get('type_coin')

            if type_coin == 'matic':
                response = transfer_rubles(from_private_key=private_key, to_public_key=to_public_key, amount=amount)
                messages.success(request, response)
            elif type_coin == 'ruble':
                response = transfer_matic(from_private_key=private_key, to_public_key=to_public_key, amount=amount)
                messages.success(request, response)
            return HttpResponseRedirect(reverse("profile"))
        else:
            messages.error(request, 'Ошибка заполнения формы')
            return HttpResponseRedirect(reverse("profile"))


class TransferNFTView(View):
    """Перевод NFT"""

    def post(self, request):
        form = TransferNFTForm(request.POST)
        account = Account.objects.get(user=self.request.user)
        private_key = account.privateKey

        if form.is_valid():
            to_account = request.POST.get('to_account')
            amount = request.POST.get('token_id')
            response = transfer_NFT(from_private_key=private_key, to_public_key=to_account, tokenId=amount)
            messages.success(request, response)
            return HttpResponseRedirect(reverse("profile"))
        else:
            messages.error(request, 'Ошибка заполнения формы')
            return HttpResponseRedirect(reverse("profile"))

############### PANEL ADMIN ###################
class PanelView(PanelAdminMixi, TemplateView):
    """Страница админа"""

    template_name = 'bank/pages/admin_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        # форма перевода денег
        context['form_coin'] = TransferCoinForm()
        context['form_NFT'] = TransferNFTForm()
        context['form_generate_NFT'] = GenerateNFTForm()
        return context
