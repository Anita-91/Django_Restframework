from django.urls import path,include
from .views import ManagerViewSet,ProjectViewSet,TaskViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'manager',ManagerViewSet)
router.register(r'project',ProjectViewSet)
router.register(r'task',TaskViewSet)
    
urlpatterns=[
    path('',include(router.urls))
]