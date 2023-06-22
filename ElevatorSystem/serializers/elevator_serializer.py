from rest_framework import serializers
from ElevatorSystem.models import ElevatorModel


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorModel
        fields = '__all__'
