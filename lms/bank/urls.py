# chat/urls.py
from django.urls import path, include, re_path
from .views.views import RedirectMainView, MainView, ProfileView, ProfileEditView, ActivitiesView, ShopView, PanelView, GenerateNFTView,\
TransferNFTView, TransferCoinView, CreateGroupView, AddUserToGroupView, RegisterUser, LoginUser, logout_user
from .views.views_django_templates import GenerateNFTAdminView, TransferNFTAdminView, TransferCoinAdminView

urlpatterns = [
    # редирект на главную страницу
    path('', RedirectMainView.as_view(), name='main'),
    path('main/', MainView.as_view(), name='main'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<slug:pk>/', ProfileEditView.as_view(), name='profile_edit'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('panel/', PanelView.as_view(), name='panel'),

    ####### NFT #############
    path('profile/generate/nft/', GenerateNFTView.as_view(), name='generate_NFT'),
    path('profile/transfer/nft/', TransferNFTView.as_view(), name='transfer_NFT'),
    path('profile/transfer/coin/', TransferCoinView.as_view(), name='transfer_coin'),
    path('panel/generate/nft/', GenerateNFTAdminView.as_view(), name='generate_NFT_admin'),
    path('panel/transfer/nft/', TransferNFTAdminView.as_view(), name='transfer_NFT_admin'),
    path('panel/transfer/coin/', TransferCoinAdminView.as_view(), name='transfer_coin_admin'),

    ######## Группы #########
    path('group/create/', CreateGroupView.as_view(), name='group_create'),
    path('group/add/', AddUserToGroupView.as_view(), name='group_add'),


]

urlpatterns_login = [
    # ///////////////// ЛОГИН /////////////////////
    path('register/', RegisterUser.as_view(), name='game_register'),
    path('login/', LoginUser.as_view(), name='game_login'),
    path('logout/', logout_user, name='game_logout'),
]

urlpatterns += urlpatterns_login
