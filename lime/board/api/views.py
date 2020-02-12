import json
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import (CreateModelMixin,
											RetrieveModelMixin,
											DestroyModelMixin)

from django.shortcuts import get_object_or_404

from . serializers import BoardSerializer, TaskSerializer
from board.models import Board, Task

def is_json(json_data):
	try:
		json.loads(json_data)
		is_valid = True
	except ValueError:
		is_valid = False
	return is_valid


class BoardDetailAPIView(DestroyModelMixin,
						RetrieveAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = BoardSerializer
	queriset = Board.objects.all()
	ordering_fields = ('title', 'create_date')
	search_fields = ('title', 'tasks__title')
	passed_id = None
	queryset = Board.objects.all()

	# def get(self, request, *args, **kwargs):
	# 	url_passed_id = request.GET.get('id', None)
	# 	json_data = {}
	# 	body_ = request.body
	# 	if is_json(body_):
	# 		json_data = json.loads(body_)
	# 	new_passed_id = json_data.get('id', None)
	# 	passed_id = url_passed_id or new_passed_id or None
	# 	if passed_id is not None:
	# 		return self.retrive(request, *args, **kwargs)
	# 	return super().get(request, *args, **kwargs)

	# def get_object(self):
	# 	request = self.request
	# 	passed_id = request.GET.get('id', None) or self.passed_id
	# 	queriset = self.get_queryset()
	# 	obj = None
	# 	if passed_id is not None:
	# 		obj = get_object_or_404()
	# 		self.object_permissions(request, obj)
	# 	return obj

	def perform_destroy(self, instance):
		if instance is not None:
			return instance.delete()
		else:
			return None

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class BoardListAPIView(CreateModelMixin,
						ListAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = BoardSerializer
	queriset = Board.objects.all()
	# ordering_fields = ('title', 'create_date')
	# search_fields = ('title', 'tasks__title')
	passed_id = None
	queryset = Board.objects.all()

	def perform_create(self, serializer):
		# serializer.save(user=self.request.user)
		serializer.save()


	def get(self, request, *args, **kwargs):
		url_passed_id = request.GET.get('id', None)
		json_data = {}
		body_ = request.body
		if is_json(body_):
			json_data = json.loads(body_)
		new_passed_id = json_data.get('id', None)
		passed_id = url_passed_id or new_passed_id or None
		if passed_id is not None:
			return self.retrive(request, *args, **kwargs)
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class TaskListAPIView(	CreateModelMixin,
						RetrieveModelMixin,
						DestroyModelMixin,
						ListAPIView):
	authentication_classes = [SessionAuthentication]
	permissions_classes = [AllowAny]
	serializer_class = TaskSerializer
	queryset = Task.objects.all()
	ordering_fields = ('title', 'create_date')
	search_fields = ('title')
	passed_id = None

	def get_object(self):
		request = self.request
		passed_id = request.GET.get('id', None) or self.passed_id
		queriset = self.get_queryset()
		obj = None
		if passed_id is not None:
			obj = get_object_or_404()
			self.object_permissions(request, obj)
		return obj

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)

	def perform_destroy(self, instance):
		if instance is not None:
			return instance.delete()
		else:
			return None

	def get(self, request, *args, **kwargs):
		url_passed_id = request.GET.get('id', None)
		json_data = {}
		body_ = request.body
		if is_json(body_):
			json_data = json.loads(body_)
		new_passed_id = json_data.get('id', None)
		passed_id = url_passed_id or new_passed_id or None
		if passed_id is not None:
			return self.retrive(request, *args, **kwargs)
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
