from django.test import TestCase
from board.models import Board, Task

class BoardTestCase(TestCase):
    def setUp(self):
        Board.objects.create(id=1, title='Test Board')

    def test_board_create_properly_url(self):
        """Board object creates a properly URL when generic view executes success_url method."""
        obj = Board.objects.get(id=1)
        self.assertEqual(obj.get_absolute_url(), '/board/1')

    def test_board_creates_active(self):
        """Board instances creates with is_active property == True"""
        obj = Board.objects.get(id=1)
        self.assertEqual(obj.is_active, True)


class TaskTestCase(TestCase):
    def setUp(self):
        Board.objects.create(id=1, title='Test Board')
        Task.objects.create(
            id=1,
            title='First title',
            text='Some description',
            board=Board.objects.get(id=1)
        )

    def test_task_creates_todo(self):
        """Task instances creates with TO DO status."""
        obj = Task.objects.get(id=1)
        self.assertEqual(obj.status, 'TD')
