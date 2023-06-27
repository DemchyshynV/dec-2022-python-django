from django.http import Http404

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all_with_cars()
    pagination_class = None

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)

        return (IsAdminUser(),)
    # permission_classes = (IsAdminUser,)


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset[0].__dict__)
    #     return queryset
    #
    # def get(self, request, *args, **kwargs):
    #     self.get_queryset()
    #     return Response('ok')


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
