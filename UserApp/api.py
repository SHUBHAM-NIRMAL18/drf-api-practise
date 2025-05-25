from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@api_view(['POST'])
def CreateUserApi(request):
    username = request.data['username']
    password = request.data['password']

    User.objects.create_user(username=username, password=password)
    return Response(
        {
            'message': 'User created successfully'
        })

@api_view(['POST'])
def LoginUserApi(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)  # Assuming you have a login function to handle session
        return Response(
            {
                'message': 'Login successful'
            })
    else:
        return Response(
            {
                'message': 'Invalid credentials'
            })

@api_view(['GET'])
def ProtectedUserApi(request):
    if request.user.is_authenticated:
        return Response(
            {
                'message': 'This is a protected route',
                'user': request.user.username
            })
    else:
        return Response(
            {
                'message': 'You are not authenticated'
            })