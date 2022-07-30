from django.shortcuts import render
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from usermanagement.models import doctor
from usermanagement import googleApi
import dateutil.parser as parser
import datetime

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

    @classmethod
    def post(cls, request):
        data = request.GET
        queryset = Event.objects.all()
        serializer = EventSerializers(data=request.data)
        creds = ""
        if serializer.is_valid():
            serializer.save()
            id = serializer.data['doctor_id']
            user = doctor.objects.get(id=id)
            username = user.username
            creds = googleApi.main(username)
            print(creds)
            service = build('calendar', 'v3', credentials=creds)
            calendar_list_entry = service.calendarList().get(calendarId='primary').execute()
            print(calendar_list_entry['summary'])
            time= datetime.datetime.strptime(serializer.data['start_time'],"%H:%M:%S")
            time = (time+timedelta(minutes=45))
            time = time.time()
            print(time)
            response = {
                "doctorname" : user.name,
                "Appoinment_Date" : serializer.data['date_appointment'],
                "Start_Time" : serializer.data['start_time'],
                "end_Time"  :  time

            }
            event = {
                'summary': f"{serializer.data['speciality']}" +"Appointment with patient",
                'description': 'Appointment with Patient',
                "end": {
                    "date": serializer.data['date_appointment']
                },
                "start": {
                    "date": serializer.data['date_appointment'],
                },
            }
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
            return Response(response)

        return Response(serializer.errors, status=400)
