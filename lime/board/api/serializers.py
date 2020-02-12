from rest_framework import serializers

from board.models import Board, Task

class BoardSerializer(serializers.ModelSerializer):
	# tasks = serializers.HyperlinkedRelatedField(
	# 								view_name='rest:task_detail',
	# 								read_only=True,
	# 								many=True
	# 							)

	class Meta:
		model = Board
		fields = [
			'id',
			'users',
			'title',
			'tasks',
		]
		read_only_fields = ['users', 'tasks']



class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = [
			'board',
			'title',
			'text',
		]
