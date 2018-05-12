from django.urls import path
from . import views

urlpatterns = [
    path('another/',views.another,name="another"),
    path('home/',views.index,name = "index"),
]

app_name = 'app'