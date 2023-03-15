from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('review/', views.review, name='blog-review'),
]
