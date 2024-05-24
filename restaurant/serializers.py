from django.db import transaction
from rest_framework import serializers

from restaurant.models import Restaurant, Menu, Dish


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "price",
            "weight",
        )
        read_only_fields = ("id",)


class MenuSerializer(serializers.ModelSerializer):

    dishes = DishSerializer(many=True, read_only=True)

    restaurant = serializers.CharField(
        source="restaurant.name",
        read_only=True,
    )

    class Meta:
        model = Menu
        fields = (
            "id",
            "restaurant",
            "date",
            "dishes",
        )
        read_only_fields = (
            "id",
            "restaurant",
        )


class MenuCreateSerializer(serializers.ModelSerializer):

    restaurant = serializers.CharField(
        source="restaurant.name",
        read_only=True,
    )

    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        source="restaurant",
        write_only=True,
    )

    dishes_id = serializers.PrimaryKeyRelatedField(
        queryset=Dish.objects.all(),
        source="dishes",
        many=True,
        write_only=True,
    )

    class Meta:
        model = Menu
        fields = (
            "id",
            "restaurant",
            "restaurant_id",
            "date",
            "dishes_id",
        )
        read_only_fields = (
            "id",
            "restaurant",
        )

    def create(self, validated_data):
        """
           Create a new Menu instance.

           This method creates a new Menu instance using the validated data provided.
           It retrieves the associated Restaurant instance from the validated data,
           creates a new Menu object, and returns it.
        """
        with transaction.atomic():

            restaurant = validated_data.pop("restaurant")
            restaurant = Restaurant.objects.get(id=restaurant.id)

            dishes_data = validated_data.pop("dishes")

            menu = Menu.objects.create(restaurant=restaurant, **validated_data)

            for dish_data in dishes_data:
                dish = Dish.objects.get(id=dish_data.id)
                menu.dishes.add(dish)

            return menu
