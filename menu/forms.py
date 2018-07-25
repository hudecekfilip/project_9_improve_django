from django import forms
from django.forms.widgets import SelectDateWidget

from . import models

class MenuForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['season', 'expiration_date', 'items']
        widgets = {
            'expiration_date': SelectDateWidget()
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = ['name']


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'description', 'standard', 'ingredients']
