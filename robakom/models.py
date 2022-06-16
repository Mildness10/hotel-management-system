from django.db import models

class HotelSystem(models.Model):
    room_number = models.IntegerField()
    amount_paid = models.IntegerField()
    occupant_name = models.CharField(max_length=200)
    occupant_email = models.EmailField()
    occupant_occupation = models.CharField(max_length=200)
    number_of_night = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.occupant_name