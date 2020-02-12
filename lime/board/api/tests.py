from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model
from board.models import Board, Task

User = get_user_model()


class BoardAPITestCase(APITestCase):
    def setUp(self):
        User.objects.create(username='testuser', 
                            password='1245',
                            )

    # def test_board_create_properly_url(self):
    #     """Board object creates a properly URL when generic view executes success_url method."""
    #     obj = Board.objects.get(id=1)
    #     self.assertEqual(obj.get_absolute_url(), '/board/1')

    # def test_board_creates_active(self):
    #     """Board instances creates with is_active property == True"""
    #     obj = Board.objects.get(id=1)
    #     self.assertEqual(obj.is_active, True)

    def test_board_create(self):
        data = {
            'title': 'new board'
        }
        url = api_reverse('rest:board')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 1)
        data_id = response.get('id')
        rud_url = api_reverse('rest:board')
        rud_data = {
            'title': 'another new board'
        }

        # get metod / retrive
        get_response = self.client.get(rud_url, rud_data, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        # put metod / update
        put_response = self.client.get(rud_url, rud_data, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        rud_response_data = put_response.data
        self.assertEqual(rud_response_data['title'], rud_data['title'])

        # delete method / delete
        del_response = self.client.delete(rud_url,  format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Board.objects.count(), 0)

        # not found
        get_response = self.client.get(rud_url, rud_data, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)