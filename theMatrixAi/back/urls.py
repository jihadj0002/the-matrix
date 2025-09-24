from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "back"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("products", views.products, name="products"),
    path("stats", views.stats, name="stats"),
    path("options", views.sett, name="options"),
    path("chats", views.c_dashboard, name="c_dashboard"),
    
    # path("contact", views.contact, name="contact"),
    # path("", views.home, name="home"),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
]
