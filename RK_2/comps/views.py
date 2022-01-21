from django.shortcuts import render
from .models import Computer, Class
from rest_framework import viewsets
from .serializers import ComputerSerializer, ClassSerializer

# Create your views here.
def main(request):
    return render(request, 'index.html', { 'data' : {
        'comps': Computer.objects.all(),
        'classes': Class.objects.all()
    }})

class CompsViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer  # Сериализатор для модели

class ClassesViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Class.objects.all()
    serializer_class = ClassSerializer  # Сериализатор для модели