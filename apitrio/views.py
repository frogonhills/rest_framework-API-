from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'matha' : 'amar shouar matha ',
        'pota' : 'amar shaouar pota'
    }
    return Response(api_urls)
    
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks , many = True)
    return Response(serializer.data)




@api_view(['GET'])
def taskDetail(request , pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks , many = False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    
    serializer = TaskSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




# https://www.youtube.com/watch?v=TmsD8QExZ84  17 min