from django.contrib import admin

from .models.elevator import ElevatorModel
from .models.elevator_request import ElevatorRequestModel
from .models.elevator_system import ElevatorSystemModel

admin.site.register(ElevatorSystemModel)
admin.site.register(ElevatorModel)
admin.site.register(ElevatorRequestModel)
