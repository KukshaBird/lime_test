from django.urls import path
from . import views

app_name = 'board-api'

urlpatterns = [
	# BOARD ENDPOINTS
    path('boards/', views.BoardListCreateAPIView.as_view(), name='board_list'),
    path('boards/<int:pk>', views.BoardDetailAPIView.as_view(), name='board_detail'),
    # TASK ENDPOINTS
    path('tasks/', views.TaskListCreateAPIView.as_view(), name='task_list'),
    path('tasks/<int:pk>', views.TaskDetailAPIView.as_view(), name='task_detail'),
]
