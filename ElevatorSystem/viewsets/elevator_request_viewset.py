from django.db.models import F, Func
import json

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ElevatorSystem.models import ElevatorRequestModel, ElevatorSystemModel, ElevatorModel
from ElevatorSystem.serializers import ElevatorRequestSerializer


class ElevatorRequestViewSet(viewsets.ModelViewSet):

    serializer_class = ElevatorRequestSerializer
    queryset = ElevatorRequestModel.objects.all()
    elevator_system = ElevatorSystemModel.objects.first()
    elevator_count = elevator_system.elevator_count
    floor_count = elevator_system.floor_count

    """method to create new requests for elevators"""
    @action(detail=True, methods=['POST'])
    def create_request(self, request):
        request_data = request.data
        are_valid_floors = self.valid_floors(request_data)

        if not are_valid_floors:
            return Response({"error":"Request has invalid floors"})       
        are_valid_requests = self.valid_requests(request_data)

        if not are_valid_requests:
            return Response({"error": "More than one request from one floor"})
        
        if self.operational_elevator_count() == 0:
            return Response({"error": "No elevator is currently operational"})
        

        assigned_elevators = self.parse_requests(request_data)  
        jsonString = json.dumps(assigned_elevators)            
        return Response(jsonString)        
    
    """method to divide requests into request sets that can be assigned parallelly"""
    def parse_requests(self, requests):
        assigned_elevators = []
        parallel_requests = []
        #number of requests that can be assigned parellelly = no. of operational elevators
        operational_elevator_count  = self.operational_elevator_count() 

        for request in requests:

            if len(parallel_requests) == operational_elevator_count:
                assigned_elevators.append(self.assign_elevators(parallel_requests))
                parallel_requests = [request]
            else:
                parallel_requests.append(request)

        if parallel_requests:
            assigned_elevators.append(self.assign_elevators(parallel_requests))
        return assigned_elevators
        

    """method to assign elevators to given set of requests parallelly"""
    def assign_elevators(self, parallel_requests):     
        available_elevators = [True for id in range(self.elevator_count)] #so that each elevator can be assigned only once per set of parallel requests
        assigned_elevators = []

        for request in parallel_requests:
            requested_from_floor = request["requested_from_floor"]
            nearest_elevator = self.get_nearest_elevator(requested_from_floor, available_elevators)

            nearest_elevator_id = nearest_elevator.elevator_id
            available_elevators[nearest_elevator_id - 1] = False #making an elevator unavailable if it has been assigned

            nearest_elevator.current_floor = request["requested_to_floor"] #assuming that elevator each the requested floor immediately
            nearest_elevator.save()

            request_object = ElevatorRequestModel(elevator = nearest_elevator, elevator_system  = self.elevator_system, requested_from_floor = request["requested_from_floor"], requested_to_floor = request["requested_to_floor"])
            request_object.save()
            assigned_elevators.append(nearest_elevator_id)
        return assigned_elevators

    """method to get nearest elevator"""
    def get_nearest_elevator(self, requested_from_floor, available_elevators):
        elevators = ElevatorModel.objects.filter(elevator_system = self.elevator_system, is_operational = True) #getting all operational elevators
        #sorting the elevators on basis of its distance from requested_from_floor
        elevators = elevators.annotate(distance = Func(F('current_floor') - requested_from_floor, function = "ABS")).order_by('distance')

        #looping to return the first available elevator from sorted elevators
        for elevator in elevators:
            id = elevator.elevator_id

            if available_elevators[id - 1]:
                return elevator
        return None    

    """method to confirm that only one request is made from one floor"""
    def valid_requests(self, requests):
        floors_requested_from = [0 for i in range(self.floor_count)]

        for request in requests:
            current_floor = request["requested_from_floor"]
            floors_requested_from[current_floor] += 1

            if floors_requested_from[current_floor] > 1:
                return False           
        return True
        
    """method to confirm that current floors are requested"""    
    def valid_floors(self, requests):
        
        for request in requests:           
            current_floor = request["requested_from_floor"]
            next_floor = request["requested_to_floor"]

            if current_floor < 0 or current_floor >= self.floor_count or next_floor < 0 and next_floor >= self.floor_count:
                return False 
        return True
    
    """method to return no. of operational elevators"""
    def operational_elevator_count(self):
        elevators = ElevatorModel.objects.filter(elevator_system = self.elevator_system, is_operational = True)
        return len(elevators)