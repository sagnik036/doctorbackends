from .models import *
from rest_framework import serializers


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = '__all__'

class UserCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = User_custom
        fields = '__all__'