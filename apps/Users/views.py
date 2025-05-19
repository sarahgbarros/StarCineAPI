from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer, SuperUserSerializer

class CreateSuperUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer
    
class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

