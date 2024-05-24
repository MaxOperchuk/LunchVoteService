from django.db import models
from django.db.models import UniqueConstraint


class Restaurant(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Menu(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menus",
    )
    date = models.DateField(auto_now_add=True)
    dishes = models.ManyToManyField(Dish, related_name="menus")

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
