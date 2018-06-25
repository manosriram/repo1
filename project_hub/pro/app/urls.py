from . import views
from django.urls import path
from app import views

urlpatterns = [
    path('courses/',views.course_view.as_view(),name="courses"),
    path('about/',views.about_view.as_view(),name="about"),
]

app_name = 'app'