from django.urls import path
from . import views

urlpatterns = [
    path('pokedex_app/', views.pokedex, name='pokedex_app'),
]
