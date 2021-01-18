# Iportamos el caso simple
from django.test import SimpleTestCase


# Create your tests here.
class SimpleTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

"""
Códigos de servicio cliente/servidor
1xx # Informativos
2xx # Aceptado
3xx # Redirecciones -> te saca de la página actual
4xx # Error de usuario
5xx # Error del servidor

Dos tipos de tests: simple y testcase

Simple: cada función está aislada y cada función es un test.
Test Case: son más comlpejos y tienen reglas con respecto a las clases.

""" 