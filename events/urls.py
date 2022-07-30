from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventView.as_view()),
]