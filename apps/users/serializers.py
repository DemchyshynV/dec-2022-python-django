from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from core.services.email_service import EmailService

from apps.users.models import UserModel as User

from .models import ProfileModel

UserModel: User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'avatar')


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {
            'avatar': {
                'required': True
            }
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at',
            'profile'
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_email(self, email: str):
        if not email.endswith('@gmail.com'):
            raise serializers.ValidationError('email must be gmail.com host')
        return email

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        EmailService.register_email(user)
        return user
