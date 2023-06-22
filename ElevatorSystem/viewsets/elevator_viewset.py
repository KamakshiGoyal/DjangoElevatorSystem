from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ElevatorSystem.models import ElevatorModel, ElevatorRequestModel
from ElevatorSystem.serializers import (ElevatorRequestSerializer,
                                        ElevatorSerializer)


class ElevatorViewSet(viewsets.ModelViewSet):

    serializer_class = ElevatorSerializer
    queryset = ElevatorModel.objects.all()
    
    """menthod to update the information of elevator"""
    @action(detail=True, methods=['POST'])
    def update_status(self, request, elevator_id):
        try:
            elevator = self.queryset.get(elevator_id = elevator_id)
            """update logic to be implemented"""
            serializer = self.get_serializer(elevator)
            return Response(serializer.data)
        except ElevatorModel.DoesNotExist:
            return Response({'error': "Elevator Doesn't Exit"}, status=404)

    """method to retrive information of elevator"""
    @action(detail=True, methods=['GET'])
    def get_status(self, request, elevator_id):
        try:
            elevator = self.queryset.get(elevator_id = elevator_id)
            serializer = self.get_serializer(elevator)
            return Response(serializer.data)
        except ElevatorModel.DoesNotExist:
            return Response({'error': "Elevator Doesn't Exit"}, status=404)
    
    """method to get all requests for a elevator"""
    @action(detail=True, methods=['GET'])
    def get_requests(self, request, elevator_id):
        all_requests = ElevatorRequestModel.objects.all()
        requests_for_elevator = all_requests.filter(elevator_id = elevator_id)
        serializer = ElevatorRequestSerializer(requests_for_elevator, many=True)
        return Response(serializer.data)
        



    
    


