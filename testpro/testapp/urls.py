from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('contact/',views.contact,name="contact"),
    path('user_login/',views.user_login,name="user_login"),
    path('info/',views.data_info,name = "info"),
    
    
]

app_name = 'testapp'