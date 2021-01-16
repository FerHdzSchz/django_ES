from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
# Es lo que se le va a mostrar al cliente, un HTML, solo DATOS, etc
# puede ser imagen, una request

def hola(request):
    return(HttpResponse('Hola Mundo!'))