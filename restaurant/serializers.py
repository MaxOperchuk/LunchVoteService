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


