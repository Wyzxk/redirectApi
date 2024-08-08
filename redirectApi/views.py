import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
       idUser = request.query_params.get('idUser')
       idPedido = request.query_params.get('idPedido')
       status = request.query_params.get('status')

       if idUser:
           print(idUser)
           print(status)
           
           # Ejemplo de cómo enviar datos a otra API usando requests
           api_url = 'http://127.0.0.1:8000/auth/check/'
           data = {
               'idUser': idUser,
               'idPedido': idPedido,
               'status': status,
           }
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

       else:
           print('nada')
           return render(request, 'index.html')
    return render(request, 'index.html')