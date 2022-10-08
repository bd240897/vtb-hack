# chat/urls.py
from django.contrib import admin
from django.urls import path, include
from .views.views import *

urlpatterns = [
    path('admin/', PanelAdminView.as_view(), name='game_logout'),
]