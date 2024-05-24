from django.utils import timezone
from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response


from restaurant.models import Restaurant, Menu, Dish

from restaurant.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    MenuCreateSerializer, DishSerializer,
)


class RestaurantListCreateView(generics.ListCreateAPIView):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishListCreateView(generics.ListCreateAPIView):

    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class MenuListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):

    queryset = Menu.objects.select_related("restaurant")
    serializer_class = MenuSerializer

    def get_serializer_class(self):

        if self.request.method == "POST":
            return MenuCreateSerializer

        return MenuSerializer

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        menus = Menu.objects.filter(date=today).prefetch_related("dishes")
        serializer = self.get_serializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
