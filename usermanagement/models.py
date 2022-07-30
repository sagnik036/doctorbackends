from django.db import models
from httplib2 import Credentials



def upload_path(instance ,filename):
    return '/'.join(['images',str(instance.name),filename]) 
# Create your models here.
class User_custom(models.Model):
    username = models.CharField(
        max_length=10,
        null = False,
        blank= False,
        unique=True
    )
    password = models.CharField(
        max_length=8,
        blank=False,
        null = False
    )

    def __str__(self):
        return self.username


class doctor(models.Model):
    username = models.CharField(
        max_length=10,
        null = False,
        blank= False,
        unique=True
    )
    password = models.CharField(
        max_length=8,
        blank=False,
        null = False
    )
    name = models.CharField(
        max_length=20,
        blank = False,
        null = False
    )
    profile_pic = models.ImageField(
        null = True,
        blank = True,
        upload_to = upload_path
    )

    def __str__(self):
        return self.username