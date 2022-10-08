from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, RedirectView, CreateView
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


class ProfileView(LoginRequiredMixin, TemplateView):
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
        print(public_key)
        # TODO delete
        # public_key = "0x0787638C8EdA33712B1FbC2dCF3dfa6603fa0C54"

        # получение баланса и истории транзакций
        context['balance'] = get_balance(public_key=public_key)
        context['balance_NFT'] = get_balance_NFT(public_key=public_key)
        context['history'] = get_history_transaction(public_key=public_key).get('history')[:10]

        # форма перевода денег
        context['form'] = TransferForm()

        return context

    def post(self, request, *args, **kwargs):
        # работа с формой для перевода денег

        # form = TransferForm(request.POST)
        # from_account = request.POST.get('from_account')
        account = Account.objects.get(user=self.request.user)
        from_account = account.privateKey

        to_account = request.POST.get('to_account')
        amount = request.POST.get('amount')
        type_coin = request.POST.get('type_coin')
        if type_coin == 'matic':
            response = transfer_rubles(from_account, to_account, amount)
            messages.success(request, response)
        elif type_coin == 'ruble':
            response = transfer_matic(from_account, to_account, amount)
            messages.success(request, response)
        elif type_coin == 'nft':
            response = transfer_NFT(from_account, to_account, tokenId=amount)
            messages.success(request, response)
        return super().get(self, request, *args, **kwargs)


class ProfileEditView(UpdateView):
    """Редактирование профиля"""

    # https://stackoverflow.com/questions/52263711/generic-view-updateview-from-django-tutorial-does-not-save-files-or-images
    template_name = 'bank/pages/profile_edit.html'
    form_class = ProfleEditForm
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse('profile')

class PanelView(TemplateView):
    """Страница админа"""

    template_name = 'bank/pages/admin_panel.html'

class ActivitiesView(TemplateView):
    """Страница активностей"""

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse("profile"))
        return super().get(self, request, *args, **kwargs)

    template_name = 'bank/pages/activities.html'

class ShopView(TemplateView):
    """Страница магазина"""

    template_name = 'bank/pages/shop.html'

# class aaa(View):
#     account = Account.objects.get(user=self.request.user)
#     from_account = account.privateKey