from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('g_auth.urls')),
    path('dashboard/', include('g_dashboard.urls')),
]
