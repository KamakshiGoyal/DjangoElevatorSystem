from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ElevatorSystem.models import (ElevatorModel, ElevatorRequestModel,
                                   ElevatorSystemModel)
from ElevatorSystem.serializers import ElevatorSystemSerializer


class ElevatorSystemViewSet(viewsets.ModelViewSet):

    serializer_class = ElevatorSystemSerializer
    queryset = ElevatorSystemModel.objects.all()

    """ method to initiate the elevator system"""
    @action(detail=True, methods=['GET'])
    def elevator_system(self, request):
            
            """checking if an elevator system already exists"""
            if not self.queryset:
                """creating a default elevator system"""
                default_elevator_system = {"system_name":"Default_Elevator_Sytem",
                                   "elevator_count": 10,
                                   "floor_count": 10}
                serializer = self.get_serializer(data = default_elevator_system)  

                if serializer.is_valid():
                    serializer.save()
                    """creating elevators for the default elevator system """
                    self.createElevators(ElevatorSystemModel.objects.first())
                    return Response(serializer.data)
                else:
                     return Response({"Some Error Occured while creating the database"})
                          
            serializer = self.get_serializer(self.queryset, many = True) 
            return Response(serializer.data)
    

    """method to create elevators for a elevator system"""
    def create_elevators(self, elevator_system):
         elevator_count = elevator_system.get().elevator_count

         if elevator_count :
            
            for elevator_id in range(elevator_count):
                ElevatorModel.objects.create(elevator_system = elevator_system, elevator_id = elevator_id + 1)
        
        




    
    


