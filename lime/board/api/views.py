from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

# from django.shortcuts import get_object_or_404

from . serializers import BoardSerializer, TaskSerializer
from board.models import Board, Task


class BoardListCreateAPIView(ListCreateAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = BoardSerializer
	queryset = Board.objects.all()
	ordering_fields = ('title', 'create_date')
	search_fields = ('title', 'tasks__title')

	def perform_create(self, serializer):
		serializer.save(users=[self.request.user])

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class BoardDetailAPIView(RetrieveDestroyAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = BoardSerializer
	queryset = Board.objects.all()

	def perform_destroy(self, instance):
		if instance is not None:
			return instance.delete()
		else:
			return None

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class TaskListCreateAPIView(ListCreateAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = TaskSerializer
	queryset = Task.objects.all()
	ordering_fields = ('title', 'create_date')
	search_fields = ('title')

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class TaskDetailAPIView(RetrieveDestroyAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = TaskSerializer
	queryset = Task.objects.all()	
