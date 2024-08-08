from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:idUser>/<str:idPedido>/<str:status>/', views.index),
    path('checkout/', views.checkout)
]
