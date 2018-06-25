from django.shortcuts import render
from django.views.generic import View,TemplateView

class base_view(TemplateView):
    template_name = 'base.html'

class index_view(TemplateView):
    template_name = 'index.html'

class course_view(TemplateView):
    template_name = 'courses.html'

class about_view(TemplateView):
    template_name = 'about.html'

    