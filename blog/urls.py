from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.add_autor, name='add_autor'),
    path('categoria/', views.add_categoria, name='add_categoria'),
    path('post/', views.add_post, name='add_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
