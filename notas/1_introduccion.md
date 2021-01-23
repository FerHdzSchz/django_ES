# ¿Qué es Django?

# 1. Iniciar un nuevo proyecto
*** django-admin startproject _<nombre>_***

## 1.1 Configuración básica y archivos de inicio
### Modificar archivo settings 
El archivo de settings se tiene que modificar como buena práctiva

  a) *APPS* 

   + MY_APPS, THIRD_APPS
   + MY_APPS = ['apps.<app_name>']  
   + INSTALLES += MY_APPS + THIRD_APPS
   + Se debe crear nueva carpeta llamada apps

  b) *TEMPLATES* 

   + En el diccionario TEMPLATES
    + Modificar DIRS : [os.path.join(BASE, 'templates')]
   + Se debe crear nueva carpeta llamada templates 


## 1.2 Agregar carpetas apps, templates y archivo init en apps

  + Crear a nivel base:
    + apps/
      + apps/\__init__\.py 
    + templates/ 
   

## 1.3 Comenzar app

python manage.py startapp <nombre_app>
mover a folder apps
registrar en settings como apps.<nombre_app>

### Si se necesita hay que agregar las urls
en el urls.py con un include


# Vistas y Templates


# Tests
En la app ver projecto pages

# Modelos
## Migrar modelos
ORM (Object Relational Map) administra mejor la base de datos
python manage.py makemigrations ***busca modelos*** y genera datos de los objetos
python manage.py migrate ***se crea la base de datos para los objetos*** que están listados con el makemigrations.

Se guardan esos objetos en la base de sqlite (se especifica en el archivo de settings)

## Creación de un modelo
models.Model y se define el tipo de modelo

## Superusuario
python manage.py createsuperuser

## Se debe registrar los modelos en el admin de la app
En el dashboard de admin para que salgan los posts en el dashboard
- en admin.py de la app
    importar el modelo en ese .py
    admin.site.register(Post)


## Se enlazan los modelos con vistas genéricas y las vistas con los templates a urls
Modificar views de la app, templates (que se direccionen a las vistas) y urls para tener accesso.

## ENlistar para views
``` python
# En el archivo views
from django.views.generic import ListView
from .models import <Modelo>


```


## CSS y estáticos



# Tarea:
## Enlistar los posts en la pag principal con los post del admin
