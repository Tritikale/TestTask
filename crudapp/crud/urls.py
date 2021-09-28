from django.urls import path
from rest_framework import routers
from .api import TaskViewset


router = routers.DefaultRouter()
router.register('task', TaskViewset, 'task')

urlpatterns = router.urls
