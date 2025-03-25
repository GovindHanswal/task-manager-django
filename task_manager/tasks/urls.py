from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet, AssignTaskAPIView, GetTasksForUserAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tasks/<int:task_id>/assign/', AssignTaskAPIView.as_view(), name='assign_task'),
    path('api/users/<int:user_id>/tasks/', GetTasksForUserAPIView.as_view(), name='user_tasks'),
]