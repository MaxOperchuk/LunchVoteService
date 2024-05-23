from django.db import models
from django.db.models import UniqueConstraint


class Restaurant(models.Model):
    """Restaurant model."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """Menu model."""

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menus",
    )
    date = models.DateField(auto_now_add=True)
    items = models.JSONField()

    class Meta:
        ordering = ["-date"]
        constraints = [
            UniqueConstraint(
                fields=[
                    "restaurant",
                    "date",
                ],
                name="unique_restaurant_date",
            )
        ]

    def __str__(self):
        return f"{self.restaurant} - {self.date}"
