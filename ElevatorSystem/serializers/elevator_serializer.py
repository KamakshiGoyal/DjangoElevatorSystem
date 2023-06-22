from rest_framework import serializers
from ElevatorSystem.models import ElevatorModel


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorModel
        fields = '__all__'
        extra_kwargs = {
            'elevator_system': { 'read_only': True },
            'elevator_id': { 'read_only': True },
            'current_floor': { 'read_only': True },
            'direction': { 'read_only': True }
        }
