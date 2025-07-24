"""Dockstring."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Dockstring."""

    class Meta:
        """Dockstring."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
