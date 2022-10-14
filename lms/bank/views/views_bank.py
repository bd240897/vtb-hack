from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, RedirectView, CreateView, FormView
from django.contrib import messages

from ..mixins.panel_admin_mixins import *
from ..models import *
from ..forms import *
from ..logic import *

# ИМПОРТ ИЗ ДРУГОГО МОДУЛЯ
from polls.views import *


class RedirectMainView(RedirectView):
    """Простой редирект на главную"""

    # https://ustimov.org/posts/11/
    def get_redirect_url(self):
        return reverse('main')

class MainView(TemplateView):
    """Главная страница"""

    template_name = 'bank/pages/main.html'

class ProfileView(PanelAdminMixin, LoginRequiredMixin, TemplateView):
    """Профиль пользователя"""

    template_name = 'bank/pages/profile.html'
    login_url = 'game_login'
    redirect_field_name = 'main'

    def get_group(self):
        """Получить список груп в которых состою"""

        dict_group = dict()
        groups = VtbGroup.objects.filter(users=self.request.user)
        print(groups)
        for group in groups:
            group_name = group.name
            dict_group[group_name] = []
            for user in group.users.all():
                dict_group[group_name].append(user.username)
        return dict_group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['its_my_page'] = True

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

        # группы
        context['groups'] = self.get_group()
        return context


class ProfileOtherUserView(PanelAdminMixin, LoginRequiredMixin, TemplateView):
    """Профиль пользователя"""

    template_name = 'bank/pages/profile.html'
    login_url = 'game_login'
    redirect_field_name = 'main'

    def get_group(self, user):
        """Получить список груп в которых состою"""

        dict_group = dict()
        groups = VtbGroup.objects.filter(users=user)
        print(groups)
        for group in groups:
            group_name = group.name
            dict_group[group_name] = []
            for user in group.users.all():
                dict_group[group_name].append(user.username)
        return dict_group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['slug'])
        print(1111111, user)
        context['its_my_page'] = False

        # данные профиля
        profile = Profile.objects.get(user=user)
        id_profile = profile.id
        context['profile'] = profile
        context['id_profile'] = id_profile

        # данные акканута
        account = Account.objects.get(user=user)
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

        # группы
        context['groups'] = self.get_group(user)
        return context

class ProfileEditView(PanelAdminMixin, UpdateView):
    """Редактирование профиля"""

    # https://stackoverflow.com/questions/52263711/generic-view-updateview-from-django-tutorial-does-not-save-files-or-images
    template_name = 'bank/pages/profile_edit.html'
    form_class = ProfleEditForm
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse('profile')


class ActivitiesView(PollsListView, PanelAdminMixin, TemplateView):
    """Страница активностей"""

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    template_name = 'bank/pages/activities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = self.get_leaderbord()
        return context

    def get_leaderbord(self):
        """Получение лидерборда по группам"""

        if not self.request.user.is_authenticated:
            return dict()
        dict_group = dict()
        groups = VtbGroup.objects.filter(users=self.request.user)
        print(groups)

        for group in groups:
            group_name = group.name
            dict_group[group_name] = []
            for user in group.users.all():
                # получим баланс
                account = Account.objects.get(user=self.request.user)
                public_key = account.publicKey
                balance = get_balance(public_key=public_key)
                # на выходе {¨name_group¨:(username, value)}
                dict_group[group_name].append((user.username, balance['maticAmount']))
            dict_group[group_name].sort(key=lambda x: str(x[1]), reverse=True)
        return dict_group


class ActivitiesPollView(PanelAdminMixin, PollView):
        """Работа с конкретным опросом по id (из модуля poll)"""

        template_name = "bank/pages/activities_poll.html"

class ShopView(PanelAdminMixin, TemplateView):
    """Страница магазина"""

    template_name = 'bank/pages/shop.html'


################# FORM VIEW ##############################

class GenerateNFTView(View):
    """Генерация NFT"""

    redirect_url_name = "profile"

    def post(self, request):

        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        private_key = account.privateKey

        form = GenerateNFTForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            response = generate_NFT(public_key, amount)
            messages.success(request, response, extra_tags="generate_NFT")
            return HttpResponseRedirect(reverse(self.redirect_url_name))
        else:
            messages.error(request, 'Ошибка заполнения формы', extra_tags="generate_NFT")
            return HttpResponseRedirect(reverse(self.redirect_url_name))


class TransferCoinView(View):
    """Перевод coin"""

    redirect_url_name = "profile"

    def post(self, request, *args, **kwargs):
        # работа с формой для перевода денег

        form = TransferCoinForm(request.POST)
        print(request.POST)
        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        private_key = account.privateKey

        if form.is_valid():
            # ищем юзера в базе денных
            to_account_name = form.cleaned_data.get('to_account')
            to_account = Account.objects.filter(user__username__icontains=to_account_name).first()
            to_public_key = to_account.publicKey

            # забираем остальные поля из запроса
            amount = form.cleaned_data.get('amount')
            type_coin = form.cleaned_data.get('type_coin')

            if type_coin == 'matic':
                response = transfer_rubles(from_private_key=private_key, to_public_key=to_public_key, amount=amount)
                messages.success(request, response, extra_tags="transfer_coin")
            elif type_coin == 'ruble':
                response = transfer_matic(from_private_key=private_key, to_public_key=to_public_key, amount=amount)
                messages.success(request, response, extra_tags="transfer_coin")
            return HttpResponseRedirect(reverse(self.redirect_url_name))
        else:
            messages.error(request, 'Ошибка заполнения формы', extra_tags="transfer_coin")
            return HttpResponseRedirect(reverse(self.redirect_url_name))


class TransferNFTView(View):
    """Перевод NFT"""
    redirect_url_name = "profile"

    def post(self, request):
        form = TransferNFTForm(request.POST)
        account = Account.objects.get(user=self.request.user)
        private_key = account.privateKey

        if form.is_valid():
            # ищем юзера в базе денных
            to_account_name = form.cleaned_data.get('to_account')
            to_account = Account.objects.filter(user__username__icontains=to_account_name).first()
            to_public_key = to_account.publicKey

            amount = form.cleaned_data.get('token_id')
            response = transfer_NFT(from_private_key=private_key, to_public_key=to_public_key, tokenId=amount)
            messages.success(request, response, extra_tags="transfer_NFT")
            return HttpResponseRedirect(reverse(self.redirect_url_name))
        else:
            messages.error(request, 'Ошибка заполнения формы', extra_tags="transfer_NFT")
            return HttpResponseRedirect(reverse(self.redirect_url_name))



