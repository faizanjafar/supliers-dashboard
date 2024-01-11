from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import AccountUser
from .serializers import RegisterUserSerializer

# Create your views here.


class RegisterUserView(generics.CreateAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
