from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from employee.models import Employee
from restaurant.models import Menu
from vote.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """Vote serializer."""

    employee = serializers.CharField(
        source="employee.email",
        read_only=True,
    )
    menu = serializers.CharField(
        source="menu.date",
        read_only=True,
    )

    class Meta:
        model = Vote
        fields = (
            "id",
            "employee",
            "menu",
            "voted_at",
        )
        read_only_fields = ("id",)


