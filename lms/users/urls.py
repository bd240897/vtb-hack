# chat/urls.py
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    # path('test/', TestView.as_view(), name='users'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('blog.urls')),
]
