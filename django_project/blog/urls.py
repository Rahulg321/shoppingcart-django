from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('review/', views.review, name='blog-review'),
    path('cart/', views.cart, name='blog-cart'),
    path('checkout/', views.checkout, name='blog-checkout')
]
