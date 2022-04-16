from os import path
from sqlite3 import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework import viewsets
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from django.http import Http404

from todoapi.serializers import TaskSerializers, Task2Serializers

from .models import Task
from django.db import transaction

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/tasks/',
        'Details': '/task/<str:pk>/',
        'Create': '/task/create/',
        'Creates': '/tasks/create/',
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


class TasksView(APIView):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = TaskSerializers(data = request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            # return Response(serializer.errors, status=400)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def createTask(self, request, *args, **kwargs):
        serializer = TaskSerializers(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    # def patch(self, request, *args, **kwargs):
    #     task = Task.objects.get(id=request.pk)
    #     serializer = TaskSerializers(instance=task, data = request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #     return Response(serializer.data)
        # return super().patch(request, *args, **kwargs)


    # def put(self, request, *args, **kwargs):
        
        # return super().put(request, *args, **kwargs)


'''
class NameView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
        '''

class TaskView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404()

    def get(self, request, *args, **kwargs):
        task = self.get_object(pk=kwargs['pk'])
        serializer = TaskSerializers(task)
        return Response(serializer.data, status = status.HTTP_200_OK)
        
    def delete(self, request, *args, **kwargs):
        task = self.get_object(pk=kwargs['pk'])
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return super().delete(request, *args, **kwargs)
