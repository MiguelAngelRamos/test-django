from django.test import TestCase
from .models import Producto
from django.core.exceptions import ValidationError
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

    def test_precio_invalido_lanza_error(self):
        producto_invalido = Producto(
            nombre="Mouse Gamer",                   # nombre válido (>= 3 chars)
            descripcion="Mouse genérico inalámbrico.",  # descripción válida (>= 10 chars)
            precio=-5.00,                            # ← INVÁLIDO: viola MinValueValidator(0.01)
            stock=10,                                # stock válido (>= 0)
            categoria="Accesorios"                   # categoría válida
        )

        with self.assertRaises(ValidationError):
            producto_invalido.full_clean()