from . import views
from django.urls import path

urlpatterns = [
    #path('login/', views.loginView, name="login"),
    #path('logout/', views.logoutView, name="logout"),
    path('register/', views.registerView, name="register"),
]

app_name = 'app'
