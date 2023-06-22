from rest_framework import serializers
from ElevatorSystem.models import ElevatorSystemModel


class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystemModel
        fields = '__all__'
        

