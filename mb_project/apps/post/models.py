from django.db import models

# Create your models here.
# Los modelos son classes

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:20]

    # funcion __str__ para que nos despliegue el nombre
    # que se aplico en el post