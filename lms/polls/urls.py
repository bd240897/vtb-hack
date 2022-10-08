# chat/urls.py
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("poll/<int:poll_id>/", PollView.as_view(), name="poll"),
    path("", PollsView.as_view(), name="polls"),
]
