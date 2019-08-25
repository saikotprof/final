from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
