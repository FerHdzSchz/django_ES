from django.views.generic import ListView
from .models import Post

# List View regresa en formato lista de diccionarios

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts' # Nombre del contexto a regresar

