from . import views
from django.urls import path, include

urlpatterns = [
    path('register/', views.registerView, name="register"),
    path('submitThis/', views.extraView, name="extra"),
]

app_name = "app"
