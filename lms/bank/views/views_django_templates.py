from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView, RedirectView
from ..models import *
from ..forms import *
from django.contrib import messages
from ..logic import *

class RedirectMainView(RedirectView):
    """Простой редирект на главную"""

    # https://ustimov.org/posts/11/
    def get_redirect_url(self):
        return reverse('main')

class TestView(TemplateView):
    template_name = 'bank/django_templates/index.html'


class MainView(TemplateView):
    template_name = 'bank/pages/main.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'bank/pages/profile.html'
    login_url = 'game_login'
    redirect_field_name = 'main'
    permission_denied_message = "aaaaaaaaaaaaaSASSSSS"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(user=self.request.user)
        id_profile = profile.id
        context['profile'] = profile
        context['id_profile'] = id_profile

        account = Account.objects.get(user=self.request.user)
        public_key = account.publicKey
        # TODO delete
        # public_key = "0x0787638C8EdA33712B1FbC2dCF3dfa6603fa0C54"

        context['balance'] = get_balance(public_key=public_key)
        context['history'] = get_history_transaction(public_key=public_key).get('history')

        context['form'] = TransferForm()

        return context

    def post(self, request, *args, **kwargs):
        form = TransferForm(request.POST)
        from_account = request.POST.get('from_account')
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
    # https://stackoverflow.com/questions/52263711/generic-view-updateview-from-django-tutorial-does-not-save-files-or-images
    template_name = 'bank/pages/profile_edit.html'
    form_class = ProfleEditForm
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse('profile')

class PanelView(TemplateView):
    template_name = 'bank/pages/admin_panel.html'

class ActivitiesView(TemplateView):
    template_name = 'bank/pages/activities.html'

class ShopView(TemplateView):
    template_name = 'bank/pages/shop.html'
