from asyncio import events
from datetime import timedelta
from django.db import models
from usermanagement.models import *
import datetime

# Create your models here.
class Event(models.Model):
    doctor_id = models.ForeignKey(
        doctor,
        on_delete=models.CASCADE
    )
    speciality = models.CharField(
        max_length=10,
        default=""
    )
    date_appointment = models.DateField()
    start_time = models.TimeField(

    )
    end_time = models.TimeField(
        null=True,
        blank=True
    )

    def save(self,*args, **kwargs):
            time= datetime.datetime.strptime(f"{self.start_time}","%H:%M:%S")
            time = (time+timedelta(minutes=45))
            self.end_time = time.time()
            super(Event, self).save(*args, **kwargs)
       

    def __str__(self):
        return self.speciality