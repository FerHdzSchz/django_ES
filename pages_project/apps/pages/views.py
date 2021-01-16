from django.shortcuts import render
from django.views.generic import TemplateView #agrega vista de emplate

# Create your views here.
# Mejor  usar clases para las visatas


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


