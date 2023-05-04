from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task, Tag
from .serializers import TaskSerializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'status': ['exact'],
        'priority': ['exact'],
        'tags__name': ['exact'],
    }
    search_fields = ['title', 'description']
    ordering_fields = ['priority', 'created_at']