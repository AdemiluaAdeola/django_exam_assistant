from django.urls import path
from quiz_app.views import *

urlpatterns = [
	path('quiz/<str:name>/', QuizListView.as_view(), name='quiz_list'),
	path('start_quiz/<int:id>/', StartQuiz.as_view(), name='start_quiz'),
	path('theory/<str:name>/<str:slug_field>/', PracticeQuestionPage.as_view(), name='theory_questions'),
]