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

# импорт из другой view
from .views_bank import GenerateNFTView, TransferNFTView, TransferCoinView


class PanelView(PanelAdminMixin, TemplateView):
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

        # Добавление в группы
        context['form_group_create'] = CreateGroupForm()
        context['form_group_add'] = AddUserToGroupForm()
        return context


class CreateGroupView(View):
    """Перевод NFT"""

    def post(self, request):
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            owner_id = form.cleaned_data.get('owner')
            name = form.cleaned_data.get('name')
            VtbGroup.objects.create(name=name, owner=User.objects.get(pk=owner_id))
            messages.success(request, f'Группа {name} создана!', extra_tags="group_create")
            return HttpResponseRedirect(reverse("panel"))
        else:
            messages.error(request, 'Ошибка заполнения формы', extra_tags="group_create")
            return HttpResponseRedirect(reverse("panel"))


class AddUserToGroupView(View):
    """Перевод NFT"""

    def post(self, request):
        form = AddUserToGroupForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data.get('user')
            user = User.objects.get(pk=user_id)
            user_name = user.username

            group_id = form.cleaned_data.get('group')
            group = VtbGroup.objects.get(pk=group_id)
            group_name = group.name

            group.users.add(User.objects.get(pk=user_id))
            messages.success(request, f'{user_name} добавлен в группу {group_name}!', extra_tags="group_add")
            return HttpResponseRedirect(reverse("panel"))
        else:
            messages.error(request, 'Ошибка заполнения формы', extra_tags="group_add")
            return HttpResponseRedirect(reverse("panel"))


class GenerateNFTAdminView(GenerateNFTView):
    """Генерация NFT"""
    redirect_url_name = "panel"


class TransferNFTAdminView(TransferNFTView):
    """Перевод NFT"""
    redirect_url_name = "panel"


class TransferCoinAdminView(TransferCoinView):
    """Перевод coin"""
    redirect_url_name = "panel"