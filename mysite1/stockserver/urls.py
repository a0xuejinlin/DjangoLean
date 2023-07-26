#stockserver/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('spec/', views.spec),
    path('dayk/', views.dayk),
]