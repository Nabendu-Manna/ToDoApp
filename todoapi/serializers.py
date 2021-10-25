from django.db.models import fields
from rest_framework import serializers
from .models import Task ,Task2

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class Task2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Task2
        fields = '__all__'
