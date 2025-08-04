from django.shortcuts import render
from quiz_app.models import *
from rest_framework.response import Response
from quiz_app.serializers import *
from rest_framework import generics, permissions, pagination
from rest_framework.views import APIView
from blog_app.models import *
from blog_app.serializers import *

# Create your views here.
class QuizHomePage(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuizListPage(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None, **kwargs):
        quiz = Quiz.objects.filter(course__name = kwargs['name'])
        serializer = QuizListSerializer(quiz, many=True,)
        return Response(serializer.data)

class StartQuiz(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__id = kwargs['pk']).order_by('?')[:100]
        serializer = QuizSerializer(question, many=True)
        return Response(serializer.data)

class PracticeQuestionPage(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None, **kwargs):
        question = PracticeQuestion.objects.filter(course__name = kwargs['name']).filter(chapter__slug = kwargs['slug_field'])
        serializer = TheorySerializer(question, many=True)
        return Response(serializer.data)

class PracticeQuestionList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None, **kwargs):
        question = PracticeQuestion.objects.filter(course__name = kwargs['name'])
        serializer = TopicSerializer(question, many=True)
        return Response(serializer.data)