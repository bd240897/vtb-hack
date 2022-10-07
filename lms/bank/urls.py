# chat/urls.py
from django.urls import path, include, re_path
from .views.views import *

urlpatterns = [
    path('bank/', TestView.as_view(), name='bank'),
]

urlpatterns_login = [
    # ///////////////// ЛОГИН /////////////////////
    path('register/', RegisterUser.as_view(), name='game_register'),
    path('login/', LoginUser.as_view(), name='game_login'),
    path('logout/', logout_user, name='game_logout'),
]

urlpatterns += urlpatterns_login