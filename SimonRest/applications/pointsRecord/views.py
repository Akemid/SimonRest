from django.shortcuts import render
from rest_framework import viewsets
from .models import Point
from .serializers import PointSerializer
# Create your views here.

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer