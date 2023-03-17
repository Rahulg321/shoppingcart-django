from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('review/', PostListView.as_view(), name='blog-review'),
    path('review/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('cart/', views.cart, name='blog-cart'),
    path('checkout/', views.checkout, name='blog-checkout'),
    path('update-item/', views.updateItem, name='update-item')
]




