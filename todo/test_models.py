from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_is_false(self):
        item = Item.objects.create(name='Test ToDo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test ToDo Item')
        self.assertEqual(str(item), 'Test ToDo Item')
