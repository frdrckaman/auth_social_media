from django.urls import path, include
from g_dashboard import views


urlpatterns = [
    path('', views.home, name="home"),
]
