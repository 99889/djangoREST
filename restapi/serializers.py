from rest_framework import serializers
from .models import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type']
