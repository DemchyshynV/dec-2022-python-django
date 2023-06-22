from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from .managers import UserManager


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user')

    USERNAME_FIELD = 'email'

    objects = UserManager()
