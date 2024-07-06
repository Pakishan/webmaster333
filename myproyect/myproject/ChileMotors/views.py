from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('registro_exitoso')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

# Vista para mostrar los pedidos
def mis_pedidos(request):
    pedidos = [
        {'id': 1, 'producto': 'Producto 1', 'cantidad': 2, 'precio': 20.00},
        {'id': 2, 'producto': 'Producto 2', 'cantidad': 1, 'precio': 15.00},
        
    ]
    return render(request, 'mis_pedidos.html', {'pedidos': pedidos})


def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html')

def blog(request):
    return render(request, 'blog.html')

def faq(request):
    return render(request, 'faq.html')


#views para base.html

from django.shortcuts import render

def home(request):
    return render(request, 'chileMotors/home.html')

def contacto(request):
    return render(request, 'chileMotors/contacto.html')

def productos(request):
    return render(request, 'chileMotors/productos.html')


#vista para carrito


from django.shortcuts import render

def home(request):
    return render(request, 'nombre_de_tu_app/home.html')

def contacto(request):
    return render(request, 'nombre_de_tu_app/contacto.html')

def productos(request):
    productos = [
        {'nombre': 'Producto 1', 'precio': 10.00, 'cantidad': 2},
        {'nombre': 'Producto 2', 'precio': 15.00, 'cantidad': 1}
    ]
    context = {
        'productos': productos
    }
    return render(request, 'nombre_de_tu_app/productos.html', context)

#base 
from django.shortcuts import render

def home(request):
    return render(request, 'my_app/home.html')

def contacto(request):
    return render(request, 'my_app/contacto.html')

def productos(request):
    return render(request, 'my_app/productos.html')

#carrito
from django.shortcuts import render

def home(request):
    return render(request, 'my_app/home.html')

def contacto(request):
    return render(request, 'my_app/contacto.html')

def productos(request):
    return render(request, 'my_app/productos.html')

#contacto
from django.shortcuts import render

def home(request):
    return render(request, 'my_app/home.html')

def contacto(request):
    return render(request, 'my_app/contacto.html')

def productos(request):
    
    productos = [
        {'nombre': 'Producto 1', 'precio': 10.00, 'cantidad': 2, 'total': 20.00},
        {'nombre': 'Producto 2', 'precio': 15.00, 'cantidad': 1, 'total': 15.00}
    ]
    context = {'productos': productos}
    return render(request, 'my_app/productos.html', context)

#datos personales

from django.shortcuts import render
from .forms import DatosPersonalesForm

def datos_personales(request):
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
           
            return render(request, 'my_app/datos_personales_confirmacion.html', {'nombre': nombre})
    else:
        form = DatosPersonalesForm()
    
    return render(request, 'my_app/datos_personales.html', {'form': form})

#index

from django.shortcuts import render

def index(request):
    return render(request, 'my_app/index.html')

def nosotros(request):
    return render(request, 'my_app/nosotros.html')

def servicios(request):
    return render(request, 'my_app/servicios.html')

def contacto(request):
    return render(request, 'my_app/contacto.html')

def productos(request):
    return render(request, 'my_app/productos.html')

#login

from django.shortcuts import render
from .models import Pedido

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'my_app/pedidos.html', {'pedidos': pedidos})
#mis pedidos

from django.shortcuts import render
from .models import Pedido

def mis_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'mis_pedidos.html', {'pedidos': pedidos})
#nosotrtos

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html')

def carrito(request):

    return render(request, 'carrito.html')

#planes

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html')

def planes(request):
    return render(request, 'planes.html')


#template
from django.shortcuts import render, get_object_or_404
from .models import Producto 
def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):

    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto.html', {'producto': producto})

#productos
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
   
    context = {
        'productos': productos  
    }
    return render(request, 'productos.html', context)

def producto_detalle(request, pk):
    
    context = {
        'producto': producto  
    }
    return render(request, 'producto.html', context)

#servivio

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    
    context = {
        'productos': productos  
    }
    return render(request, 'productos.html', context)

#template p
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    # Aquí puedes implementar lógica para mostrar productos desde la base de datos si es necesario
    return render(request, 'productos.html')
