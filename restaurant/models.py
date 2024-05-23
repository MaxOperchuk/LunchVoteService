from django.db import models
from django.db.models import UniqueConstraint


class Restaurant(models.Model):
    """Restaurant model."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



# Create your models here.
