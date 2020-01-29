from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    title = models.CharField(max_length=255, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name='boards')

    def __str__(self):
        return self.title

class Task(models.Model):

    STATUS = [
        ('TD', 'TO DO'),
        ('PR', 'In progress'),
        ('DN', 'Done'),
    ]

    title = models.CharField(max_length=255, null=True)
    text = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS, default='TD')
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    board = models.ForeignKey(Board, related_name='tasks', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
