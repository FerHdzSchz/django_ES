from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class BlogListView(ListView):
    # Regresa una lista de elementos
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    # Regresa un elemento a partir de la llave primaria
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'
