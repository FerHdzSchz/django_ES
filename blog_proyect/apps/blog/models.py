from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE) 
    # Cuando se elimine algo que dependa del modelo lo demás que depende de éste
    body = models.TextField()

    def __str__(self):
        return self.title
        # Para desplegar el titulo en el dashboard