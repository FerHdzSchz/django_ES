# ¿Qué es Djang?

# 1. Iniciar un nuevo proyecto
django-admin startproject <nombre>

## Modificar archivo settings 
El archivo de settings se tiene que modificar como buena práctiva
MY_APPS, THIRD_APPS INSTALLES +=
templates = [os.path.join(BASE_, 'templates')]

## Agregar carpetas apps, templates
__init__.py en apps

## Si se necesita hay que agregar las urls
en el urls.py con un include


# comenzar app
python manage.py startapp <nombre_app>
mover a folder apps
registrar en settings como apps.<nombre_app>


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



# Tarea:
## Enlistar los posts en la pag principal con los post del admin
