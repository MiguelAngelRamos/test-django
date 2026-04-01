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

    def test_formulario_valido_sin_imagen_url(self):
        datos = DATOS_VALIDOS.copy()
        datos.pop('imagen_url')  # El campo imagen_url es opcional
        form = ProductoForm(data=datos)
        self.assertTrue(form.is_valid(), msg=f"Errores inesperados: {form.errors}")

    def test_nombre_muy_corto_es_invalido(self):
        datos = {**DATOS_VALIDOS, 'nombre': 'Te'}  # spread operator esparse todas las keys con su valores para copiar y modificar solo el campo 'nombre'
        form = ProductoForm(data=datos)
        self.assertFalse(form.is_valid(), msg=f"Errores esperados: {form.errors}")
        self.assertIn('nombre', form.errors)
        self.assertIn("El nombre debe tener al menos 3 caracteres reales.", form.errors['nombre'][0])

    
    def test_nombre_solo_espacios_es_invalido(self):
        datos = {**DATOS_VALIDOS, 'nombre': '                    '}
        form = ProductoForm(data=datos)
        self.assertFalse(form.is_valid(), msg=f"Errores esperados: {form.errors}")
        self.assertIn('nombre', form.errors)
        # self.assertIn("El nombre debe tener al menos 3 caracteres reales.", form.errors['nombre'][0])