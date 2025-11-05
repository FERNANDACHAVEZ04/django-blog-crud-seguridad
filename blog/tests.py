from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        self.post = Post.objects.create(
            title="Título de prueba", body="Contenido de prueba", author=self.user
        )

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Título de prueba")
        self.assertEqual(f"{self.post.body}", "Contenido de prueba")
        self.assertEqual(f"{self.post.author}", "testuser")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)  # Redirige al Login

    def test_post_detail_view(self):
        response = self.client.get(f"/post/{self.post.pk}/")
        self.assertEqual(response.status_code, 302)