from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from toDo.models import ToDoItem

# Create tests here
def createItem(client):
    url = reverse('todoitem-list')
    data = {'title': 'Walk the dog'}
    return client.post(url, data, format='json')

class TestCreateTodoItem(APITestCase):
    """
    Ensure we can create a new todo ToDoItem
    """
    def setUp(self):
        self.response = createItem(self.client)

    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_reveived_location_header_hyperlink(self):
        self.assertRegexpMatches(self.response['Location'], '^http://.+/toDos/[\d]+$')

    def test_item_was_created(self):
        self.assertEqual(ToDoItem.objects.count(), 1)

    def test_item_has_correct_title(self):
        self.assertEqual(ToDoItem.objects.get().title, 'Walk the dog')


class TestUpdateTodoItem(APITestCase):
    """
    Ensure we can update an existing todo item using PUT
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(ToDoItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Walk the dog', 'completed': True}
        self.response = self.client.put(url, data, format='json')

    def test_received_200_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(ToDoItem.objects.get().completed, True)


class TestPatchToDoItem(APITestCase):
    """
    Ensure we can update an existing todo item using PATCH
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(ToDoItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Walk the dog', 'completed': True}
        self.response = self.client.patch(url, data, format='json')

    def test_received_200_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(ToDoItem.objects.get().completed, True)

class TestDeleteToDoItem(APITestCase):
    """
    Ensure we can update an Delete todo item using Delete
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(ToDoItem.objects.count(), 1)
        url = response['Location']
        self.response = self.client.delete(url)

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_item_was_deleted(self):
        self.assertEqual(ToDoItem.objects.count(), 0)

class TestDeleteAllToDoItems(APITestCase):
    """
    Ensure we can delete all items
    """

    """def setUp(self):
        createItem(self.client)
        createItem(self.client)
        self.assertEqual(ToDoItem.objects.count(), 2)
        self.response = self.client.delete(reverse('todoitem-list'))

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_item_was_deleted(self):
        self.assertEqual(ToDoItem.objects.count(), 0)"""
