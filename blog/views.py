from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Vista para listar todos los posts
class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    login_url = "login"

# Vista para ver el detalle de un post
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    login_url = "login"

# Vista para crear un nuevo post
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body"]
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Vista para eliminar un post
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user