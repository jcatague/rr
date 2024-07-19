from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time}"
