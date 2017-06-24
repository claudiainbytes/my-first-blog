from django.shortcuts import render

# Create your views here.

#Crear un metodo def llamado
#post_list que recibe una peticion,
#request y devuelve return, un
#metodo render que renderizara o construira la
#plantilla
def post_list(request):
    return render(request, 'blog/post_list.html', {})
