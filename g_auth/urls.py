from django.contrib import admin
from django.urls import path, include
from g_auth import views


urlpatterns = [
    path('', views.login, name="home"),
]
