from django.db import models


class ElevatorSystemModel(models.Model):
    """Model class for Elevator system"""
    system_name = models.CharField(max_length=100)
    elevator_count = models.IntegerField(default=1)
    floor_count = models.IntegerField(default=1)

    def __str__(self):
        return self.system_name
