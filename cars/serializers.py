from rest_framework import serializers

from .models import CarModel


class CarBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=25)
    year = serializers.IntegerField()


class CarAllSerializer(CarBaseSerializer):
    pass


class CarSerializer(CarBaseSerializer):
    seat_count = serializers.IntegerField()
    body_type = serializers.CharField(max_length=25)
    engine_volume = serializers.FloatField()

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data: dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)

        instance.save()
        return instance
