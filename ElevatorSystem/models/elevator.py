from django.db import models


class ElevatorModel(models.Model):
    """Model class for Elevator"""
    elevator_system = models.ForeignKey('ElevatorSystemModel', on_delete=models.CASCADE)
    elevator_id = models.IntegerField()
    current_floor = models.IntegerField(default=1)
    is_door_open = models.BooleanField(default=True)
    direction = models.CharField(choices=[('UP', 'UP'), ('DOWN', 'DOWN'), ('STANDING', 'STANDING')], default='STANDING', max_length=50)
    is_operational = models.BooleanField(default=True)

    class Meta:
        """Meta class for Elevator Requests"""
        db_table = 'elevator'
        ordering = ['elevator_id']

    def __str__(self):
        return str(self.elevator_id)
    
    
    


