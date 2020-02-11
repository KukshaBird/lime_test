from rest_framework import serializers

from board.models import Board, Task

class BoardSerializer(serializers.ModelSerializer):
	tasks = serializers.HyperlinkRelatedField(
									sourse='tasks',
									view_name='rest:task_detail',
									read_only=True,
									many=True
								)

	class Meta:
		model = Board
		fields = [
			'users',
			'title',
			'tasks',
		]
		read_only_fields = ['users']



class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = [
			'board',
			'title',
			'message',
		]
