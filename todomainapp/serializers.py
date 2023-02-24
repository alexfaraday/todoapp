from rest_framework import serializers
from .models import hometasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=hometasks
        fields='__all__'
