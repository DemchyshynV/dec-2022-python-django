from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
