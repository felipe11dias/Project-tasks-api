from core.api.v1.serializers.serializers_v1 import TasksSerializers
from django.http.response import HttpResponse
from django.shortcuts import render
from typing import Generic
from django.db.models.fields import GenericIPAddressField
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework import generics
from core.models import Task


class ListTasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializers

class DetailTasksView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializers


def index(request):
    return HttpResponse("Funcionando")

