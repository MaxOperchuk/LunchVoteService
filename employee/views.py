from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken

from employee.serializers import EmployeeSerializer, AuthTokenSerializer


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = ()


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


class ManageEmployeeView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer

    def get_object(self):
        return self.request.user
