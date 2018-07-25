from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Ingredient, Menu, Item

class IngredientModelsTests(TestCase):
    def test_ingredient_creation(self):
        ingredient = Ingredient.objects.create(
            name = "cibule"
        )
        self.assertEqual(ingredient.name, "cibule")


class ItemModelsTests(TestCase):
    def test_item_creation(self):
        item = Item.objects.create(
            name = "Svickova",
            description = "test",
            standard = False,
        )
        self.assertEqual(item.name, "Svickova")
        self.assertEqual(item.description, "test")
        self.assertEqual(item.standard, False)


class MenuModelsTests(TestCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(
            season = "FS18",
            expiration_date = "2018-07-20"
        )
        self.assertEqual(menu.season, "FS18")

    def setUp(self):
        ingredient1 = Ingredient(name="cibule")
        ingredient1.save()
        self.item1 = Item(
            name = "Svickova",
            description = "test"
        )
        self.item1.save()
        self.menu1 = Menu.objects.create(
            season = "FS18",
            expiration_date = "2018-07-20"
        )
        self.menu1.items.add(self.item1)

    def test_menu_list(self):
        resp = self.client.get(reverse('menu:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.menu1, resp.context['menus'])
        self.assertTemplateUsed(resp, 'menu_list.html')
        self.assertContains(resp, self.menu1.season)

    def test_edit_menu(self):
        resp = self.client.get(reverse('menu:edit', kwargs={'pk': self.menu1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu_detail.html')
