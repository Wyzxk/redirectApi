from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import requests

@api_view(['GET'])
def index(request, idUser, idPedido, status):
    # Realizar la petición a la API después de renderizar la respuesta
    api_url = 'http://127.0.0.1:8000/auth/check/'
    data = {
        'idUser': idUser,
        'idPedido': idPedido,
        'status': status,
    }
    
    try:
        # Hacer la petición a la API
        api_response = requests.post(api_url, data=data)
        if api_response.status_code == 200:
            print('Datos enviados correctamente a la API')
        else:
            print('Error al enviar datos a la API:', api_response.status_code)
    except requests.RequestException as e:
        print(f'Error en la solicitud a la API: {e}')
    
    return render(request,'index.html',{
        'idUser': idUser,
        'idPedido': idPedido,
        'status': status,
    })
        
def checkout(request):
    return render(request, 'index2.html')