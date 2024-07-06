from django.urls import path
from . import views
urlpatterns = [

]
#base
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    
]

#carrito
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
   
]

#contacto
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    
]
#datos personales 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.datos_personales, name='datos_personales'),

]

#index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    # Otras rutas según sea necesario
]

#login

from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.lista_pedidos, name='pedidos'),
    
]

#mis pedidos
from django.urls import path
from . import views

urlpatterns = [
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    # Otros paths según sea necesario
]


#nosotros

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    # Otros paths según sea necesario
]

#planes

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    path('planes/', views.planes, name='planes'),
]

#temaplte

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    # Añade más rutas según sea necesario
]

#productos
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
]

#servicio

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
]

#temaplte p
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
]
