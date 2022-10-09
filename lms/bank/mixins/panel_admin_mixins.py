from ..models import *

class PanelAdminMixin():
    """Cоздадим админу профиль с кошельком"""

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            if not Account.objects.filter(user=self.request.user).exists():
                account = Account.objects.create(user=self.request.user)
                account.create_wallet()
                self.public_key = account.publicKey
                self.private_key = account.privateKey
            if not Profile.objects.filter(user=self.request.user).exists():
                Profile.objects.create(user=self.request.user)
        return super().dispatch(request, *args, **kwargs)