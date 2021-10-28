import json
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from . import models, serializers


class BoardViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test999", "password")
        self.client.force_authenticate(self.user)
        self.valid_board = {
            "title": "testing",
            "context": "aaaaaaasssvvvvbbb",
        }
        self.board_qs = models.Board.objects.create(title="Casting", context=33333333, user=self.user)
        self.valid_update_board = {
            "title": "update_completed",
            "context": "power overwhelming",
        }

        def create_board(self):
            res = self.client.post("/board/", data=json.dump(self.valid_board), content_type="application/json")
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        def all_board_list(self):
            res = self.client.get("/board/")
            test_board = models.Board.objects.all()
            serializer = serializers.BoardSerializer(test_board)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, serializer.data)

        def filter_title_board_list(self):
            res = self.client.get("/board/")
            test_board = models.Board.objects.filter(title__icontains="Cast", context__icontains=3)
            serializer = serializers.BoardSerializer(test_board)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, serializer.data)

        def update_board(self):
            res = self.client.patch(
                "/board/",
                kwargs={"pk": self.board_qs.pk},
                data=json.dump(self.valid_update_board),
                content_type="application/json",
            )
            self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

