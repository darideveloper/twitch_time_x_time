from . import views
from django.urls import path

urlpatterns = [
    path('donations/', views.get_donations, name='donations'),
    path('disable-user/<name>/', views.disable_user, name='disable_user'),
    path('update-donation/<int:id>/', views.upodate_donation, name='update_donation'),
]