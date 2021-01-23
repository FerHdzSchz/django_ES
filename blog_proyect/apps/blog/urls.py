from django.urls import path, include
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'), # Coma al final
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    # el path del post pide solo un elemento que es entero
]

