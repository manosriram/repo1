from django.shortcuts import render
from django.views.generic import View,TemplateView

class base_view(TemplateView):
    template_name = 'base.html'

class index_view(TemplateView):
    template_name = 'index.html'
