from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ElevatorSystem.models import ElevatorRequestModel
from ElevatorSystem.serializers import ElevatorRequestSerializer


class ElevatorRequestViewSet(viewsets.ModelViewSet):

    serializer_class = ElevatorRequestSerializer
    queryset = ElevatorRequestModel.objects.all()

    """method to create new request for elevator"""
    @action(detail=True, methods=['POST'])
    def create_request(self, request):

        """logic to be implemeted"""
        serializer = self.get_serializer(self.queryset, many = True) 
        return Response(serializer.data)