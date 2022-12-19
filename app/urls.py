# mysite/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
]