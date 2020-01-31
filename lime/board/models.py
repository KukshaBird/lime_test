from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

User = get_user_model()


class Board(models.Model):
    title = models.CharField(max_length=255, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name='boards', blank=True)
    is_active = models.BooleanField(default=True)

    @mark_safe
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:board_detail', kwargs={'pk': self.id})


class Task(models.Model):

    STATUS = [
        ('TD', 'TO DO'),
        ('PR', 'In progress'),
        ('DN', 'Done'),
    ]

    title = models.CharField(max_length=150, null=True)
    text = models.TextField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS, default='TD')
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    board = models.ForeignKey(Board, related_name='tasks', null=True, on_delete=models.CASCADE)

    @mark_safe
    def __str__(self):
        return self.title
