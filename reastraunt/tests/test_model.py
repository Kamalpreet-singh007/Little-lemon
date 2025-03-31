from reastraunt.models import Menu_table 
from reastraunt.serializers import MenuSerializer 
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.item1 = Menu_table.objects.create(Title="Pizza", price=200, inventory=50)
        self.item2 = Menu_table.objects.create(Title="Burger", price=100, inventory=30)

    def test_get_all_(self):
        response = self.client.get(reverse('get_all_menu_items'))  
        items = Menu_table.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

        
