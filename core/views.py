from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

# SE LISTAN LOS PRODUCTOS
def index(request):
    productosAll = Producto.objects.all().order_by('nombreProducto') # SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 5) # CANTIDAD POR PAGINA
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'listado': productosAll,
        'paginator': paginator
    }

    return render(request, 'core/index.html', data)

def carrito(request):

    return render(request, "core/carrito.html")



