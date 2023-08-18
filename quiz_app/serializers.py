from rest_framework import serializers
from quiz_app.models import *
from blog_app.serializer import TopicSerializer

class QuizListSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    #quiz = serializers.HyperlinkedIdentityField(view_name='start_quiz',lookup_field = "id",)
    class Meta:
        model = Quiz
        fields = [
            'id',
            'topic',
            'name',
            #'quiz',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'choice',
            'correct',
        ]

class QuizSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'answer',
        ]

class TheorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeQuestion
        fields = [
            'id',
            'question',
            'answer',
        ]
#practice-list