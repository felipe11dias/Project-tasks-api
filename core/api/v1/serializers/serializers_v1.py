from django.db import models
from django.db.models import fields
from rest_framework import serializers;
from core.models import Task


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id','title','nome',
        )

