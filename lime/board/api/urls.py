from django.urls import path
from . import views

urlpatterns = [
    path('boards/', views.BoardListAPIView.as_view()),
    path('tasks/', views.TaskListAPIView.as_view()),
]
