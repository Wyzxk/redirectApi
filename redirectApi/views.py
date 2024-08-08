from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import requests

@api_view(['GET'])
def index(request, idUser, idPedido, status):
    # Aquí ya no se verifica si idUser tiene valor
    print(idUser)
    print(status + "hoal")
    
    # Ejemplo de cómo enviar datos a otra API usando requests
    api_url = 'http://127.0.0.1:8000/auth/check/'
    data = {
        'idUser': idUser,
        'idPedido': idPedido,
        'status': status,
    }
    try:
        response = requests.post(api_url, data=data)
        if response.status_code == 200:
            print('Datos enviados correctamente a la API')
            # Pasar las variables a la plantilla
            return render(request, 'index.html', {
                'usuario': idUser,
                'pedido': idPedido,
                'estado': status,
            })
        else:
            print('Error al enviar datos a la API:', response.status_code)
            return render(request, 'index.html', {
                'error': 'Error al enviar datos a la API.'
            })
    except requests.RequestException as e:
        print(f'Error en la solicitud a la API: {e}')
        return render(request, 'index.html', {
            'error': 'Error al conectar con la API.'
        })
        
def checkout(request):
    return render(request, 'index2.html')