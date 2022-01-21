from .models import Computer, Class
from rest_framework import serializers

class ComputerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ["model", "count", "classroom"]

class ClassSerializer (serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "name"]