from unittest import TestCase
from productos.forms import ProductoForm
# Datos bases reutilizables
DATOS_VALIDOS = {
    'nombre': 'Teclado Mecánico',
    'descripcion': 'Un teclado con luces RGB excelente',
    'precio': 120.50,
    'stock': 15,
    'categoria': 'Accesorios',
    'imagen_url': 'https://example.com/teclado.jpg'
}

class ProductoFormTest(TestCase):
    def test_formulario_valido_con_datos_completos(self):
        form = ProductoForm(data=DATOS_VALIDOS)
        self.assertTrue(form.is_valid(), msg=f"Errores inesperados: {form.errors}")