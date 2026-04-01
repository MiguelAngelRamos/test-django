from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class CuentasViewsTest(TestCase):
    def setUp(self):
        self.cliente = Client()

    def test_vista_registro_carga_correctamente(self):
        response = self.cliente.get(reverse('registro'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_creacion_usuario_falla_con_password_debil(self):
        data = {
            'username': 'testuser',
            'password1': '123',
            'password2': '123',
        }
        response = self.cliente.post(reverse('registro'), data)
       
        self.assertEqual(response.status_code, 200)
        self.assertIn('password2', response.context['form'].errors)
        errors_password = response.context['form'].errors['password2']

        self.assertTrue(
            any("La contraseña es demasiado corta" in error for error in errors_password) or
            any("Esta contraseña es demasiado común" in error for error in errors_password) or
            any("Esta contraseña es completamente numérica" in error for error in errors_password)
        )
    