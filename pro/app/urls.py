from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name="about"),
    path('latest/',views.Latest.as_view(),name="latest"),
    path('all_vid/',views.Allvid.as_view(),name="all_vid"),
    path('contact/',views.signup,name="contact"),
    path('comments/',views.comment_view,name="comments"),
    path('data/',views.feedback_data,name="user_data"),
    path('fill_form/',views.buy_view,name="fill_in"),
    path('feed/',views.bot_com,name="review"),
    path('register/',views.register_view,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),


]

app_name = 'app'