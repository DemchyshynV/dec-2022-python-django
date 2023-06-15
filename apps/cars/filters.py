from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.serializers import ValidationError
from .models import CarModel


def car_filtered_queryset(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case _:
                raise ValidationError({'detail': f'"{k}" not allowed here'})
    return qs
