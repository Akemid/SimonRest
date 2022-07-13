from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Point
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'is_staff']

class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        fields = [
            'username','level'
        ]