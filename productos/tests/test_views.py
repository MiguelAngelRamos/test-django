from django.test import TestCase, Client
from productos.models import Producto
from django.urls import reverse
from django.contrib.auth.models import User
class ProductViewsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        cls.producto = Producto.objects.create(
            nombre='Teclado Mecánico',
            descripcion='Un teclado con luces RGB excelente',
            precio=120.50,
            stock=15,
            categoria='Accesorios',
            imagen_url='https://example.com/teclado.jpg'
        )
        
    def setUp(self):
        self.cliente = Client() # crea un cliente de prueba para simular solicitudes HTTP

    def test_lista_productos_es_publica(self):
        response = self.cliente.get(reverse('producto_list'))

        # Confirmar http 200 ok 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teclado Mecánico')