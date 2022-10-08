# chat/urls.py
from django.urls import path, include, re_path
from .views.views import *

urlpatterns = [
    # редирект на главную страницу
    path('', RedirectMainView.as_view(), name='main'),
    path('main/', MainView.as_view(), name='main'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<slug:pk>/', ProfileEditView.as_view(), name='profile_edit'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('panel/', PanelView.as_view(), name='panel'),
    path('profile/transfer/nfr', TransferNFTView.as_view(), name='transfer_NFT'),
]

urlpatterns_login = [
    # ///////////////// ЛОГИН /////////////////////
    path('register/', RegisterUser.as_view(), name='game_register'),
    path('login/', LoginUser.as_view(), name='game_login'),
    path('logout/', logout_user, name='game_logout'),
]

urlpatterns += urlpatterns_login