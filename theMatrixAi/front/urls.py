from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
