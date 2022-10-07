# chat/urls.py
from django.urls import path, include, re_path
from .views.views import *

urlpatterns = [
    path('test/', TestView.as_view(), name='bank'),
]

