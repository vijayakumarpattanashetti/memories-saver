from django.test import TestCase
from .models import Memories
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """Test suite for the the memories model."""
    def setUp(self):
        #define the test client and other test variables
        user = User.objects.create(username="bob")
        self.memories_text = "Had a wonderful one day trip to Goa"
        self.memories = Memories(text=self.memories_text, owner=user) #specify the owner

    def test_model_can_create_memories(self):
        #test the memories model if it can create memories
        old_count = Memories.objects.count()
        self.memories.save()
        new_count = Memories.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        #test if readable string is returned
        self.assertEqual(str(self.memories), self.memories_text)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        #define the test client and other test variables
        user = User.objects.create(username="bob")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.memories_data = {'text': 'Amazing Wonderla Exprience', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.memories_data,
            format="json")

    def test_model_can_create_memories(self):
        #test the api for creation capability
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        #test user authorization
        new_client = APIClient()
        res = new_client.get('/memories/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_model_can_get_memories(self):
        #test the api if it can get given memories
        memories = Memories.objects.get(id=1)
        response = self.client.get('/memories/', kwargs={'pk': memories.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, memories)

    def test_model_can_update_memories(self):
        #test the api if it can update given memories
        memories = Memories.objects.get()
        change_memories = {'text': 'Amazing Wonderla'}
        res = self.client.put(
            reverse('details', kwargs={'pk': memories.id}),
            change_memories, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_model_can_delete_memories(self):
        #test the api if it can delete given memories
        memories = Memories.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': memories.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
