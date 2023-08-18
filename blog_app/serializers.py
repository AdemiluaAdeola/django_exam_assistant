from .models import *
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = [
            'id',
            'name',
        ]

class CourseSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(read_only=True, many=True)
    class Meta:
        model = Courses
        fields = [
            'id',
            'name',
            'topics',
        ]

class OutlineSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    class Meta:
        model = Outline
        fields = [
            'topic',
            'date',
            'body',
        ]