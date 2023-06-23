from rest_framework import serializers
from ElevatorSystem.models import ElevatorRequestModel


class ElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequestModel
        fields = ('elevator', 'elevator_system', 'requested_from_floor', 'requested_to_floor',)
        extra_kwargs = {
            'elevator': { 'read_only': True },
            'elevator_system': { 'read_only': True }

        }
