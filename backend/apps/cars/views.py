from django.utils.decorators import method_decorator

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from core.permission.is_superuser import IsSuperUser

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[],))
class CarListView(ListAPIView):
    """
        Get all Cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.my_objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by id
    put:
        Full update Car by id
    patch:
        Partial update Car bi id
    delete:
        Delete Car by id
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
