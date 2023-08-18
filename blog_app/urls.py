from django.urls import path
from blog_app.views import *

urlpatterns = [
    path('courses/', CourseListView.as_view(), name="courses"),
    path('topic/<str:name>/', TopicListView.as_view(), name="topics")
    path('outline/<int:id>/', OutlineView.as_view(), name="outline"),
]