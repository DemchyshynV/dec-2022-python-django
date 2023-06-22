from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from apps.users.models import UserModel as User

from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
