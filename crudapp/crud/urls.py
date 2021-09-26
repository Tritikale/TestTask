from django.urls import path
from rest_framework import routers
from .api import TaskListView


router = routers.DefaultRouter()
router.register('task', TaskListView, 'task')

urlpatterns = router.urls
