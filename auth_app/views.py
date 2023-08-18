from rest_framework import permissions, generics
from auth_app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
class ChangePasswordView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateUserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if user.is_authenticated:
            return qs.filter(username = user.username)
        else:
            return User.objects.none()
