from datetime import datetime

from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel

from .choices.body_type_choices import BodyTypeChoices


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=25, validators=(
        V.RegexValidator(RegExEnum.BRAND.pattern, RegExEnum.BRAND.msg),
    )
                             )
    body = models.CharField(max_length=11, choices=BodyTypeChoices.choices)
    price = models.IntegerField(validators=(
        V.MinValueValidator(0),
        V.MaxValueValidator(1000000)
    ))
    year = models.IntegerField(validators=(
        V.MinValueValidator(1990),
        V.MaxValueValidator(datetime.now().year)
    ))
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
