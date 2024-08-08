from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import requests

@api_view(['GET'])
def index(request, idUser, idPedido, status):
    if idUser:
        return render(request,'index.html')
    else: 
        return render(request,'index2.html')
    # La vista ahora recibe parámetros de URL directamente
    # if idUser:
    #     print(idUser)
    #     print(status)
        
    #     # Ejemplo de cómo enviar datos a otra API usando requests
    #     api_url = 'http://127.0.0.1:8000/auth/check/'
    #     data = {
    #         'idUser': idUser,
    #         'idPedido': idPedido,
    #         'status': status,
    #     }
    #     response = requests.post(api_url, data=data)
    #     if response.status_code == 200:
    #         print('Datos enviados correctamente a la API')
    #         # Pasar las variables a la plantilla
    #         return render(request, 'index.html', {
    #             'usuario': idUser,
    #             'pedido': idPedido,
    #             'estado': status,
    #         })
    #     else:
    #         print('Error al enviar datos a la API:', response.status_code)
    #         return render(request, 'index.html', {
    #             'error': 'Error al enviar datos a la API.'
    #         })

    # else:
    #     print('nada')
    #     return render(request, 'index.html', {
    #         'error': 'No se proporcionaron los parámetros necesarios.'
    #     })

def checkout(request):
    return render(request, 'index2.html')