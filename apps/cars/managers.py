from django.db import models


class CarQuerySet(models.QuerySet):
    def get_cars_by_auto_park_id(self, pk):
        return self.filter(auto_park_id=pk)

    def get_only_kia(self):
        return self.filter(brand='Kia')

    def year_less(self, year):
        return self.filter(year__lt=year)


class CarManager(models.Manager):

    def get_queryset(self):
        return CarQuerySet(self.model)

    def get_cars_by_auto_park_id(self, pk):
        return self.get_queryset().get_cars_by_auto_park_id(pk)

    def get_only_kia(self):
        return self.get_queryset().get_only_kia()

    def year_less(self, year):
        return self.get_queryset().year_less(year)
