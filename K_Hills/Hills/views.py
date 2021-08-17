from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from .models import RecipePost


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class FormPageView(TemplateView):
    template_name = 'form.html'


class RecipePostView(ListView):
    model = RecipePost
    template_name = 'recipe_posts.html'


class PostDetailView(DetailView):
    model = RecipePost
    template_name = 'detail.html'
