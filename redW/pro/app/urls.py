from . import views
from django.urls import path, include

urlpatterns = [
    path("register/", views.registerView, name="register"),
    path("submitThis/", views.formView, name="form"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("info/", views.grabView, name="info"),
]

app_name = "app"
