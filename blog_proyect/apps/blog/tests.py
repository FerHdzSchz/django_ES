from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse # Redireccionador de url
from .models import Post

# Create your tests here.
class BlogTest(TestCase):
    def setUp(self): #Siempre configurar el setup
        self.user = get_user_model().objects.create_user(
            username = 'Fer',
            email = 'test@gmail.com',
            password = 'secret'

        )
        self.post = Post.objects.create(
            title='post_test',
            body='esto es una prueba',
            author=self.user,
        )
    
    def test_string_representation(self): # Para revisar que se creo bien el post
        post = Post(title = 'post_test')
        self.assertEqual(str(post), post.title)
        # str se define en la clase del modelo para que regrese el titulo
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}",  'post_test')
        self.assertEqual(f"{self.post.body}",   'esto es una prueba')
        self.assertEqual(f"{self.post.author}", 'Fer')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'esto es una prueba')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail(self):
        no_response = self.client.get('post/100/')
        self.assertEqual(no_response.status_code, 404)
        
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'esto es una prueba')
        self.assertTemplateUsed(response, 'post_detail.html')
