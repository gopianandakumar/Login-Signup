from django.contrib import admin
from django.urls import path, include
from .views import authView, home
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    
]
