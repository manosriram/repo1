from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('contact/',views.contact,name="contact"),
]

app_name = 'testapp'