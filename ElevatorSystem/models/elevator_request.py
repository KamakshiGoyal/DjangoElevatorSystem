from django.db import models

class ElevatorRequestModel(models.Model):
    """Model class for Elevator Requests"""
    elevator = models.ForeignKey('ElevatorModel', on_delete = models.CASCADE)
    elevator_system = models.ForeignKey('ElevatorSystemModel', on_delete = models.CASCADE)
    requested_from_floor = models.IntegerField()
    requested_to_floor = models.IntegerField()

    class Meta:
        """Meta class for Elevator Requests"""
        db_table = 'elevator_request'
        ordering = ['elevator_id']

    def __str__(self):
        return 'Request to floor' + str(self.requested_to_floor)  + 'from' + str(self.requested_from_floor)
