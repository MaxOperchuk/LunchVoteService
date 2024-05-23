from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from employee.serializers import EmployeeSerializer, AuthTokenSerializer


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = ()

# Create your views here.
