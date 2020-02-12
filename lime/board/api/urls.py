from django.urls import path
from . import views

app_name = 'rest'

urlpatterns = [
    path('boards/', views.BoardListAPIView.as_view(), name='board_list'),
    path('boards/<int:pk>', views.BoardDetailAPIView.as_view(), name='board_list'),
    path('tasks/', views.TaskListAPIView.as_view(), name='task_list'),
]
