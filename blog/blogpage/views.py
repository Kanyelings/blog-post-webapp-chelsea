from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
class HomeBlogView(ListView):
    model = Post
    template_name = 'HomePage.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'PostDetail.html'
