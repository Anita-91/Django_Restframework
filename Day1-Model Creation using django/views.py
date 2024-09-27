
from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Manager, Project, Task
from .serializers import ManagerSerializer, ProjectSerializer, TaskSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
    filter_backends=[filters.SearchFilter]
    search_fields=['name','email']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
