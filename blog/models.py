#Libreria para trabajar tipos de datos del modelo
from django.db import models
#Libreria para trabajar zona horarias
from django.utils import timezone

#Definicion del modelo Post, hereda de la clase models
class Post(models.Model):
    #Definicion de datos del modelo
    #ForeignKey relaciona el id del autor con el modelo Post
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #Metodo para publicar un post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #Metodo que retorna el titulo del post    
    def __str__(self):
        return self.title

# Create your models here.
