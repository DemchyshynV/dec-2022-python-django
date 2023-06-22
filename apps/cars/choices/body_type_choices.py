from django.db import models


class BodyTypeChoices(models.TextChoices):
    Hatchback = "Hatchback",
    Sedan = "Sedan",
    MUV_SUV = "MUV / SUV",
    Coupe = "Coupe",
    Convertible = "Convertible",
    Wagon = "Wagon",
    Van = "Van",
    Jeep = "Jeep",
