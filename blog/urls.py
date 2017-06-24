#Importa la funcion url de django
from django.conf.urls import url
#Importa todas las vistas de la aplicacion blog
from . import views

#Asigna una vista view llamada post_list a la URL ^$.
#'http://127.0.0.1:8000/'
#name='post_list' identifica la vista
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
