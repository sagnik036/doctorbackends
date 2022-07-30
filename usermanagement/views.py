from socket import SocketIO
from django.shortcuts import render
from rest_framework.response import Response
from .models import doctor
from .serializers import DoctorSerializers
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle
from . import googleApi

class DoctorView(ListCreateAPIView):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializers

    @classmethod
    def post(cls,request):
        data = request.GET
        queryset = doctor.objects.all()
        serializer = DoctorSerializers(data=request.data)
        # username = serializer.validated_data['username']
        try:
            if serializer.is_valid():
                serializer.save()
                username = serializer.data['username']
                print(username)
                googleApi.main(username)
                return Response(serializer.data)
        except:
            return Response(serializer.errors)
