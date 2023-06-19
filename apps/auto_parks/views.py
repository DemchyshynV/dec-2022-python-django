from django.http import Http404
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkCarListCreateView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        if not AutoParkModel.objects.filter(pk=pk).exists():
            raise Http404()

        cars = CarModel.objects.filter(auto_park_id=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # auto_park = self.get_object()
        exists = AutoParkModel.objects.filter(pk=pk).exists()

        if not exists:
            raise Http404()

        serializer.save(auto_park_id=pk)
        return Response(serializer.data, status.HTTP_201_CREATED)
