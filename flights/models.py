from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
    
# Create your models here.
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.PositiveIntegerField()  # duration in minutes
    
    def __str__(self):
        return f"{self.origin} to {self.destination} ({self.duration} mins)"
    

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"