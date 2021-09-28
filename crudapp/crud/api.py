from .models import Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer
from .permissions import IsAuthor


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TaskSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
