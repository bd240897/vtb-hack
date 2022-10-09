# chat/urls.py
from django.urls import path, include, re_path
from .views import *

# урлы для теста
urlpatterns = [
    path("poll/<int:poll_id>/", PollView.as_view(), name="poll"),
    path("", PollsListView.as_view(), name="polls"),
]
