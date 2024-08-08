from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import requests

@api_view(['GET'])
def index(request, idUser, idPedido, status):
    # Aquí ya no se verifica si idUser tiene valor
    return render(request, 'index.html',{
        'idUser':idUser,
        'idPedido':idPedido,
        'status':status,
    })
        
def checkout(request):
    return render(request, 'index2.html')