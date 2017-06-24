from django.contrib import admin
from .models import Post

#Incluimos el modelo Post para que sea visible en la pagina
#del administrador
admin.site.register(Post)
