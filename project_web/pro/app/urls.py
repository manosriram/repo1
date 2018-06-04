from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name="about"),
    path('latest/',views.Latest.as_view(),name="latest"),
    path('all_vid/',views.Allvid.as_view(),name="all_vid"),
    path('contact/',views.signup,name="contact"),
    path('comments/',views.comment_view,name="comments"),
    path('data/',views.feedback_data,name="user_data"),
  
]

app_name = 'app'