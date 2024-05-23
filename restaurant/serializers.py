from django.db import transaction
from rest_framework import serializers

from restaurant.models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    """Restaurant serializer."""

    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class MenuSerializer(serializers.ModelSerializer):
    """Menu serializer."""

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
            "items",
        )
        read_only_fields = (
            "id",
            "restaurant",
        )


class MenuCreateSerializer(serializers.ModelSerializer):
    """Menu create serializer."""

    restaurant = serializers.CharField(
        source="restaurant.name",
        read_only=True,
    )
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        source="restaurant",
        write_only=True,
    )

    class Meta:
        model = Menu
        fields = (
            "id",
            "restaurant",
            "restaurant_id",
            "date",
            "items",
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
            menu = Menu.objects.create(restaurant=restaurant, **validated_data)
            return menu
