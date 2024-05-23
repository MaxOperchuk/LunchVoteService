from django.shortcuts import render
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



# Create your views here.
