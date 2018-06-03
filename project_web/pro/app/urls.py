from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name="about"),
    path('latest/',views.Latest.as_view(),name="latest"),
    path('all_vid/',views.Allvid.as_view(),name="all_vid"),
    path('contact/',views.signup,name="contact"),
    path('send/',views.sending_mail,name="sending"),
  
]

app_name = 'app'