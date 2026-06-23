from django.test import Client, TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Bruschetta", price=12.50, inventory=50)
        Menu.objects.create(title="Greek Salad", price=10.00, inventory=40)
        Menu.objects.create(title="Pasta", price=15.00, inventory=30)

        self.client = APIClient()
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
