from django.test import TestCase
from .models import Post
# Create your tests here.

class PostModelCase(TestCase):

    def setUp(self):
        Post.objects.create(text = 'Just a text') 
        # No interfiere con la base de datos
    
    def test_text_content(self):
        post = Post.objects.get(id = 1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Just a text')
        # Se obtienen los datos del primer objeto de la base de datos referente 
        # al Post
    
         