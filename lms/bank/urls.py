# chat/urls.py
from django.urls import path, include, re_path
from .views.views import *

urlpatterns = [
    # path('main/', MainView.as_view(), name='main'),
    # path('bank/', TestView.as_view(), name='bank'),

    path('main/', MainView.as_view(), name='main'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<slug:pk>/', ProfileEditView.as_view(), name='profile_edit'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('panel/', PanelView.as_view(), name='panel'),
]

urlpatterns_login = [
    # ///////////////// ЛОГИН /////////////////////
    path('register/', RegisterUser.as_view(), name='game_register'),
    path('login/', LoginUser.as_view(), name='game_login'),
    path('logout/', logout_user, name='game_logout'),
]

urlpatterns += urlpatterns_login