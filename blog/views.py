from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Vista para listar todos los posts
class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    login_url = "login"

# Vista para mostrar un solo post
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    login_url = "login"