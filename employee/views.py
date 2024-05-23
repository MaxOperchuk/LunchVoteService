from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from employee.serializers import EmployeeSerializer, AuthTokenSerializer


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = ()


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AuthTokenSerializer


class ManageEmployeeView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer

    def get_object(self):
        return self.request.user
