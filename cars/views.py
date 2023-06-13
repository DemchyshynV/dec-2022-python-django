from django.forms import model_to_dict
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CarModel
from .serializers import CarSerializer


# class TestOneView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('Hello from get')
#
#     def post(self, *args, **kwargs):
#         body = self.request.data
#         print(body)
#         params_dict = self.request.query_params.dict()
#         print(params_dict, 'params_dict')
#         return Response('Hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('Hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('Hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('Hello from delete')
#
#
# class TestTwoView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         print(pk)
#         return Response('sdfsfdsdf')

# CRUD
# Create
# Read/Retrieve
# Update
# Delete/Destroy


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        # res = [model_to_dict(car) for car in cars]
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # car = CarModel(**data)
        # car.save()
        # print(serializer.data)
        # car = CarModel.objects.create(**serializer.data)
        # serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data: dict = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data: dict = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data, partial=True)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()

        return Response(status=status.HTTP_204_NO_CONTENT)
