from django.urls import path
from app import views


urlpatterns = [
    path('register/',views.register,name="register"),
]

app_name = 'app'