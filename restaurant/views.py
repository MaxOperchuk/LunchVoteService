from django.utils import timezone
from rest_framework import generics, status, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Restaurant, Menu
from restaurant.permissions import IsAdminOrIfAuthenticatedReadOnly
from restaurant.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    MenuCreateSerializer,
)


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.select_related("restaurant")
    serializer_class = MenuSerializer
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):

        if self.action == "create":
            return MenuCreateSerializer

        return self.serializer_class


class CurrentDayMenuView(APIView):
    permission_classes = (IsAuthenticated,)

# Create your views here.
    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        menus = Menu.objects.filter(date=today)
        serializer = MenuSerializer(menus, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


