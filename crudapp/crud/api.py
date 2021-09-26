from .models import Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer


class TaskListView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TaskSerializer
