from rest_framework import serializers

from board.models import Board, Task

class BoardSerializer(serializers.ModelSerializer):

	tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='board-api:task_detail'
    )

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
			'id',
			'board',
			'title',
			'text',
			'status',
		]
