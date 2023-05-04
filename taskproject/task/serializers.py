from .models import Task, Tag
from rest_framework import serializers




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'created_at', 'status', 'updated_at', 'tags']