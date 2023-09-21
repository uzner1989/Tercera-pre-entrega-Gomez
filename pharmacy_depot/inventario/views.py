from django.shortcuts import render, get_object_or_404
from .models import Producto, Cliente
from inventario.forms import ProductoForm, ClienteForm
from inventario.forms import BuscarForm


def index(request):
    # Lógica para la página de inicio (si es necesario)
    return render(request, 'templates/inventario/index.html')

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'templates/inventario/producto_list.html', {'productos': productos})

def producto_detail(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'templates/inventario/producto_detail.html', {'producto': producto})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'templates/inventario/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'templates/inventario/cliente_detail.html', {'cliente': cliente})

def buscar(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            # Realizar la búsqueda en la base de datos según los criterios del formulario
            # Luego, mostrar los resultados en una plantilla de resultados de búsqueda
            # y renderizarla aquí.
            pass
    else:
        form = BuscarForm()
    
    return render(request, 'templates/inventario/buscar.html', {'form': form})
