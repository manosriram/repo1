from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('register/',views.register_view,name="register"),
    path('post/',views.post_view,name="post"),
    path('profile/',views.post_view1,name="profile"),
]


app_name = 'app'