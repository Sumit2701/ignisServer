from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

@api_view(['POST'])
def event_create(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response({"message": "Username and password are required"}, status=400)

    existing_user = User.objects.filter(username=username).first()
    if existing_user:
        return Response({"message": "Username already exists"}, status=409)

    hashed_password = make_password(password)
    new_user = User(username=username, password=hashed_password)
    new_user.save()

    return Response({"message": "User registered successfully"}, status=201)

@api_view(['POST'])
def login(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = User.objects.filter(username=username).first()
    if not user or not check_password(password, user.password):
        return Response({"message": "Invalid username or password"}, status=409)

    return Response({"username": username}, status=200)