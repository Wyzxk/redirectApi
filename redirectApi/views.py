from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



def index(request):
    return render(request, 'index.html')  # Asegúrate de que el nombre del archivo coincida

@api_view(['POST'])
@permission_classes([AllowAny])
def sendMessage(request):
    if request.method == 'POST':
        email = request.data.get('email')
        name = request.data.get('name')
        topic = request.data.get('topic')
        message = request.data.get('message')

        # Verificar que se proporcionen todos los datos
        if email and name and topic and message:
            # Enviar el correo
            eTopic = topic
            eMessage = f"Mensaje: {message}\nNombre: {name}\nEmail: {email}"
            eEmail = settings.EMAIL_HOST_USER
            recipient = ["jhonkerteje1@gmail.com"]

            try:
                send_mail(eTopic, eMessage, eEmail, recipient)
                return Response({'message': 'Correo enviado correctamente'}, status=200)
            except Exception as e:
                return Response({'error': f'Error al enviar el correo: {str(e)}'}, status=500)
        else:
            return Response({'error': 'Faltan datos en el formulario'}, status=400)
