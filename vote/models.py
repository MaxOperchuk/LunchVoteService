from django.db import models
from django.conf import settings
from restaurant.models import Menu
from django.db.models import UniqueConstraint


class Vote(models.Model):
    """Vote model."""

    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    voted_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-voted_at"]
        constraints = [
            UniqueConstraint(
                fields=[
                    "employee",
                    "voted_at",
                ],
                name="unique_employee_voted_at",
            )
        ]

    def __str__(self):
        return f"{self.employee} - {self.menu}"
