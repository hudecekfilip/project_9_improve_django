from django.shortcuts import render

from .models import Menu, Item, Ingredient

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})
