from django.test import TestCase

# Create your tests here.
from django.test import TestCase
#base

class MyTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_app/home.html')
        
#carrito

from django.test import TestCase


class MyTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_app/home.html')
        
#conatcto

from django.test import TestCase

class MyTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_app/home.html')
        

#nosotros
from django.test import TestCase
from django.urls import reverse

class IndexPageTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

  
#planes

from django.test import TestCase
from django.urls import reverse

class ServiciosPageTests(TestCase):
    def test_servicios_view_status_code(self):
        url = reverse('servicios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    

#template
from django.test import TestCase
from django.urls import reverse
from .models import Producto

class ProductoTests(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(nombre='Rueda de automovil', descripcion='Descripción del producto...', precio=1329.00)

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detalle_producto_view(self):
        url = reverse('detalle_producto', args=[self.producto.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rueda de automovil')

#productos

from django.test import TestCase
from django.urls import reverse

class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_productos_view(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)

#servciios
from django.test import TestCase
from django.urls import reverse

class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_productos_view(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)

#temaplte p

from django.test import TestCase
from django.urls import reverse

class ChileMotorsViewsTestCase(TestCase):
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_nosotros_view(self):
        response = self.client.get(reverse('nosotros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nosotros.html')
    
    def test_servicios_view(self):
        response = self.client.get(reverse('servicios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'servicios.html')
    
    def test_contacto_view(self):
        response = self.client.get(reverse('contacto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacto.html')
    
    def test_productos_view(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos.html')
