from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', HomeBlogView.as_view(), name='home'),
]