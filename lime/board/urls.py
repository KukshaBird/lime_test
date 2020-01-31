from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    #  BOARDS
    path('', views.BoardListView.as_view(), name='board_list'),
    path('board_create/', views.BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>', views.BoardDetailView.as_view(), name='board_detail'),
    #  TASKS
    path('task_update/<int:pk>', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task_move/<int:pk>', views.TaskMoveView.as_view(), name='task_move'),
    path('task_delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task_create/<int:board_pk>', views.TaskCreateView.as_view(), name='task_create'),
]
