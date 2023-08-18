from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.
class CourseListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

class OutlineView(APIView):
    def get(self, request, format=None, **kwargs):
        outline = Outline.objects.filter(topic__id = kwargs['id']).first()
        serializer = OutlineSerializer(instance=outline)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TopicListView(APIView):
    def get(self, request, format=None, **kwargs):
        outline = Topic.objects.filter(course__name = kwargs['name'])
        serializer = OutlineSerializer(instance=outline, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)