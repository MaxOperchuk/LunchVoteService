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


