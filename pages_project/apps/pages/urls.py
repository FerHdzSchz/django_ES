
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'Home'), # en ruta home, la clase 
    path('about/', AboutPageView.as_view(), name = "About")
]
