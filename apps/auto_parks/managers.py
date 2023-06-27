from django.db import models


class AutoParkManager(models.Manager):
    def all_with_cars(self):
        return self.prefetch_related('cars')
