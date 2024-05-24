from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from employee.models import Employee
from restaurant.models import Menu
from vote.models import Vote


TODAY = timezone.now().date()


class VoteSerializer(serializers.ModelSerializer):

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


class VoteCreateSerializer(VoteSerializer):

    employee = serializers.CharField(
        source="employee.email",
        read_only=True,
    )

    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.filter(date=TODAY),
        source="menu",
        write_only=True,
    )

    class Meta:
        model = Vote
        fields = (
            "id",
            "employee",
            "menu",
            "menu_id",
            "voted_at",
        )
        read_only_fields = ("id", "employee", "menu")

    def create(self, validated_data):
        """Create a new vote instance."""

        with transaction.atomic():
            menu = validated_data.pop("menu")
            menu = Menu.objects.get(id=menu.id)

            employee = Employee.objects.get(id=self.context["request"].user.id)

            vote = Vote.objects.create(
                employee=employee,
                menu=menu,
                **validated_data,
            )

            return vote

    def validate(self, attrs):
        """
        Validate that the vote for this employee
        and menu on the voted_at date is unique.
        """

        data = super(VoteSerializer, self).validate(attrs=attrs)
        employee = self.context["request"].user

        if Vote.objects.filter(
                employee_id=employee.id, voted_at=TODAY
        ).exists():

            raise serializers.ValidationError(
                "You have already voted menu today."
            )

        return data
