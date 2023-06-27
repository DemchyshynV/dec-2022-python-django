from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.users.models import UserModel as User

from .filters import UserFilter
from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all_with_profiles()
    filterset_class = UserFilter
    permission_classes = (AllowAny,)
