from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model
from board.models import Board, Task
from rest_framework.test import APIClient

User = get_user_model()


class BoardAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='TestUser', password='1245')

    def create_item(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'new board',
        }
        url = api_reverse('board-api:board_list')
        response = self.client.post(url, data, format='json')
        return response

    def test_board_create(self):
        response = self.create_item()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 1)
        
    def test_board_get(self):
        """
        get metod / retrive
        """
        data = self.create_item().data
        data_id = data.get('id')
        rud_url = api_reverse('board-api:board_detail', kwargs={'pk': data_id})
        rud_data = {
            'title': 'another new board'
        }
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_board_put_patch(self):
        """
        put and patch metod / update
        """
        data = self.create_item().data
        data_id = data.get('id')
        rud_url = api_reverse('board-api:board_detail', kwargs={'pk': data_id})
        rud_data = {
            'title': 'another new board'
        }
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        patch_response = self.client.patch(rud_url, rud_data, format='json')
        self.assertEqual(patch_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_board_delete(self):
        """
        delete method / delete
        """
        data = self.create_item().data
        data_id = data.get('id')
        rud_url = api_reverse('board-api:board_detail', kwargs={'pk': data_id})
        rud_data = {
            'title': 'another new board'
        }
        del_response = self.client.delete(rud_url,  format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Board.objects.count(), 0)

        # not found
        get_response = self.client.get(rud_url, rud_data, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='TestUser', password='1245')
        Board.objects.create(title='test_board')

    def create_item(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'new task',
            'text': 'some test text',
            'board': self.user.id,

        }
        url = api_reverse('board-api:task_list')
        response = self.client.post(url, data, format='json')
        return response

    def test_task_create(self):
        response = self.create_item()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        
    def test_task_get(self):
        """
        get metod / retrive
        """
        response = self.create_item()
        data_id = response.data.get('id')
        rud_url = api_reverse('board-api:task_detail', kwargs={'pk': data_id})
        rud_data = {
            'title': 'another new task',
            'text': 'long-long text',
            'board': self.user.id,
        }
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_task_put_patch(self):
        """
        put and patch metod / update
        """
        response = self.create_item()
        data_id = response.data.get('id')
        rud_url = api_reverse('board-api:task_detail', kwargs={'pk': data_id})
        rud_data = {
            'title': 'another new task',
            'text': 'long-long text',
            'board': self.user.id,
        }
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        patch_response = self.client.patch(rud_url, rud_data, format='json')
        self.assertEqual(patch_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertNotEqual(response.data['title'], rud_data['title'])

    def test_task_delete(self):
        """
        delete method / delete
        """
        response = self.create_item()
        data_id = response.data.get('id')
        rud_url = api_reverse('board-api:task_detail', kwargs={'pk': data_id})
        rud_data = {
            'title': 'another new task',
            'text': 'long-long text',
            'board': self.user.id,
        }
        del_response = self.client.delete(rud_url,  format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

        # not found
        get_response = self.client.get(rud_url, rud_data, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
