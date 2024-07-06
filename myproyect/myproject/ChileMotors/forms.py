# base
from django import forms
from .models import Producto

# Example form
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']

#carrito
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad']
#contacto
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad']

#datos personales 
from django import forms

class DatosPersonalesForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Email')
    telefono = forms.CharField(label='Teléfono', max_length=15)

#login 

from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'fecha_pedido', 'total']


#mis pedidos
from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero', 'fecha_pedido', 'total']

#nosotros

from django import forms

class AgregarProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)
