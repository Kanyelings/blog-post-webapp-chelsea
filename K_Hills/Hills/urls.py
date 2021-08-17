from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form/', FormPageView.as_view(), name='form'),
    path('recipe/', RecipePostView.as_view(), name='post'),
    path('recipe/<int:pk>/', PostDetailView.as_view(), name='detail'),
]
