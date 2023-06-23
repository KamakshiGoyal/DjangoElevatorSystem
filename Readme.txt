## ElevatorSystem
This is an Elevator Management System made using Django Rest Framework.
The system is initialized with 10 elevators and 10 floors. It maintains the functioning and states of all elevators and assign the most optimal elevator for the given request.


## Use the following steps to run the project locally

1.Virtual Environment - Open a terminal and use the following command to create a virtual environment.
python -m venv venv
Now activate the virtual environment with the following command.

# windows machine
venv\Scripts\activate.bat

#mac/linux
source venv/bin/activate

2. Packages and requirements - to install the required pakages run the following code.

pip install /requirements.txt

3. Runing the server - use the following code to run the project.

 python manage.py runserver


## Using the system.

use the following URLs to connect to endpoints.

1. "[port]/elevatorsystem/" : GET
This endpoint returns the Default Elevator Management System.

[
    {
        "id": 2,
        "system_name": "Default_Elevator_Sytem",
        "elevator_count": 10,
        "floor_count": 10
    }
]

2. "[port]/elevatorsystem/requestelevator/" : POST
This endpoint submits the list of requests for an elevator:
[
    {
        "requested_from_floor": 6,
        "requested_to_floor": 5

    }
]

It will return the list of assigned elevators

3. "[port]/elevatorsystem/elevator/<int:elevator_id>/" : GET
This endpoint will get the status information of the given elevator

{
    "id": 3,
    "elevator_id": 3,
    "current_floor": 6,
    "is_door_open": false,
    "direction": "STANDING",
    "is_operational": false,
    "elevator_system": 2
}

4. "[port]/elevatorsystem/elevator/update/<int:elevator_id>/" : POST
This endpoint can be used to manage and update the status of an elevator
{
    "is_door_open": false,
    "is_operational": false
}

5. "[port]/'elevatorsystem/elevator/allrequests/<int:elevator_id>/": GET
This endpoint is used to get all requests of a given elevator

[
    {
        "elevator": 2,
        "elevator_system": 2,
        "requested_from_floor": 1,
        "requested_to_floor": 5
    },
    {
        "elevator": 2,
        "elevator_system": 2,
        "requested_from_floor": 3,
        "requested_to_floor": 6
    },
    {
        "elevator": 2,
        "elevator_system": 2,
        "requested_from_floor": 6,
        "requested_to_floor": 3
    }
]


## Models and attributes

1. ElevatorSystemModel: [id, system_name, elevator_count, floor_count]

By default the system has one model as follows:
{
    system_name: "Default_Elevator_Sytem",
    elevator_count: 10,
    floor_count: 10
}
   
2. ElevatorModel: [id, elevator_system, elevator_id, current_floor, is_door_open, direction, is_operational ]

3. ElevatorRequestModel: [id, elevator, elevator_system, requested_from_floor, requested_to_floor]


## Design 

Each Elevator System has n no. of elevators (one to many relationships) and each elevator can take certain Requests(one to many relationships).
By default, there is only one Elevator System with 10 elevators and 10 floors. Since each elevator and each request uses elevator_system
as a foreign key in the future, the project can be expanded to add more than one Elevator System.
Users will submit a list of requests. At a given time elevators which operational will be assigned.
Requests will be handled in sets. Each Request Set will be assigned parrallely i.e for each each request in request set a different elevator will be assigned.
Request made first will be assigned first.
It is assumed that once the elevator is assigned it will immediately reach the requested floor.

## Assumptions

1. All transit time is considered negligible.
2. An elevator will process only one request at a time.
3. Each floor has only 1 button to call an elevator. So at a given time at most 10 requests will be made for our Default Elevator System
4. All elevators work parrallelly.

