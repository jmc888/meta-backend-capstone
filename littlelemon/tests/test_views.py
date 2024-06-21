import random
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from littlelemonAPI.models import MenuItem
from django.contrib.auth.models import User


def create_random_menuitems(num_menuitem):
    menuitem_list = []
    for i in range(num_menuitem):
        menuitem = MenuItem.objects.create(
            title=f"name{random.randint(100, 1000)}",
            price=random.randint(1, 50),
            inventory=random.randint(1, 5),
        )
        menuitem_list.append(menuitem)
    return menuitem_list


class MenuViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="12345")
        self.url = reverse("menu-items")
        num_menuitem = 10
        self.menuitem_list = create_random_menuitems(num_menuitem)

    def test_menuitem_list_with_authentication(self):
        self.client.login(username="test", password="12345")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        menuitems_expected_list = self.menuitem_list
        menuitems_result_list = response.data
        self.assertEqual(len(menuitems_result_list), len(menuitems_expected_list))

        for i in range(len(menuitems_expected_list)):
            menuitem_exp = menuitems_expected_list[i]
            menuitem_res = menuitems_result_list[i]

            self.assertEqual(menuitem_exp.title, menuitem_res["title"])

    def test_menuitem_list_without_authentication(self):
        # Make a GET request to the view without logging in
        response = self.client.get(self.url)

        self.assertNotEqual(response.status_code, 200)
