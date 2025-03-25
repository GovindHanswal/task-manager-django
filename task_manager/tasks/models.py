from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=50, choices=[
        ('backend', 'Backend'), ('frontend', 'Frontend'), ('testing', 'Testing')
    ])

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
