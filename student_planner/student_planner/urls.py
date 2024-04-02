"""
URL configuration for student_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
   path("admin/", admin.site.urls),
   path("accounts/", include("allauth.urls")), 
   path("account/" , views.AccountView.as_view(), name="account"),
   path("login/", views.LoginView.as_view(), name="login"),
   path("register/", views.RegisterView.as_view(), name="register"),
   path("", include("planner.urls")),
]
