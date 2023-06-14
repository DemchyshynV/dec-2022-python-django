from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seat_count = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine_volume = models.FloatField()
