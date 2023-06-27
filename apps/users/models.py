from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from .managers import UserManager


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50, validators=[
        V.RegexValidator(RegExEnum.NAME.pattern, RegExEnum.NAME.msg)
    ])
    surname = models.CharField(max_length=50, validators=[
        V.RegexValidator(RegExEnum.NAME.pattern, RegExEnum.NAME.msg)
    ])
    age = models.IntegerField(validators=[
        V.MinValueValidator(16),
        V.MaxValueValidator(150),
    ])


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(RegExEnum.PASSWORD.pattern, RegExEnum.PASSWORD.msg)
    ])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
