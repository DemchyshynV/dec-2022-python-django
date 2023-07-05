from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from _testcapi import raise_exception

from core.permission import IsAdminOrWriteOnlyPermission, IsSuperUser
from core.services.email_service import EmailService

from apps.users.models import UserModel as User

from .filters import UserFilter
from .serializers import AvatarSerializer, UserAvatarListSerializer, UserSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all_with_profiles()
    filterset_class = UserFilter
    permission_classes = (IsAdminOrWriteOnlyPermission,)

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)


# class UserAddAvatarView(GenericAPIView):
#     serializer_class = UserAvatarListSerializer
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context |= {'profile': self.request.user.profile}
#         return context
#
#     def post(self, *args, **kwargs):
#         serializer = self.get_serializer(data=self.request.FILES)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)

class UserAddAvatarView(CreateAPIView):
    serializer_class = UserAvatarListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context |= {'profile': self.request.user.profile}
        return context


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user: User = self.get_object()
        if user:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BlockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BlockAdminUserView(BlockUserView):
    permission_classes = (IsSuperUser,)


class UnBlockAdminUserView(UnBlockUserView):
    permission_classes = (IsSuperUser,)


class TestEmail(GenericAPIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(*args, **kwargs):
        EmailService.test_email()
        return Response('ok')
