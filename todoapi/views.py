from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status

from todoapi.serializers import TaskSerializers, Task2Serializers

from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/tasks/',
        'Details': '/task/<str:pk>/',
        'Create': '/task/create/',
        'Create': '/task/create/',
    }

    return Response(api_urls)

@api_view(['GET'])
def tasksList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['get'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    print(task)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PATCH'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task2Create(request):
    serializer = Task2Serializers(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
