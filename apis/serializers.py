from rest_framework import serializers
from .models import TODO

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = ['id', 'title', 'description', 'priority', 'is_completed']
