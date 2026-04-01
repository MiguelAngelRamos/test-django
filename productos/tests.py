from django.test import TestCase
from .models import Producto
# Create your tests here.
class ProductoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.producto_base = Producto.objects.create(
            nombre='Teclado Mecánico',
            descripcion='Un teclado con luces RGB excelente',
            precio=120.50,
            stock=15,
            categoria='Accesorios',
            imagen_url='https://example.com/teclado.jpg'
    )

    def test_producto_str_method(self):
        # necesito self por que debo utilizar los asserts de TestCase
        producto = self.producto_base
        resultado = str(producto)
        esperado = "Teclado Mecánico (Accesorios)"
        self.assertEqual(resultado, esperado)