from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

class CreateTaskAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignTaskAPIView(APIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        user_ids = request.data.get('assigned_users', [])
        users = User.objects.filter(id__in=user_ids)

        if not users.exists():
            return Response({"error": "One or more users do not exist."}, status=status.HTTP_400_BAD_REQUEST)

        task.assigned_users.add(*users)
        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)

class GetTasksForUserAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer