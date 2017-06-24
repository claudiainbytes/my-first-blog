from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

#Crear un metodo def llamado
#post_list que recibe una peticion,
#request y devuelve return, un
#metodo render que renderizara o construira la
#plantilla
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
