from django.contrib import admin
from django.urls import path

from .views import index, success_view

urlpatterns = [
    path('', index, name='index'),
    path('success/', success_view, name='success'),
]