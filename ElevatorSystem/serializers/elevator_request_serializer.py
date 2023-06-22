from rest_framework import serializers
from ElevatorSystem.models import ElevatorRequestModel


class ElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequestModel
        fields = '__all__'
