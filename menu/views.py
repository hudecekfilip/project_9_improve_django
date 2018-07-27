from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from . import models
from . import forms

def menu_view(request):
    menus = models.Menu.objects.all().prefetch_related('items__ingredients')
    return render(request, 'menu_list.html', {'menus': menus})


def menu_detail(request, pk):
    instance = models.Menu.objects.prefetch_related('items').get(pk=pk)
    items = models.Item.objects.all().prefetch_related('ingredients')
    form = forms.MenuForm(instance=instance)
    if request.method == 'POST':
        form = forms.MenuForm(request.POST, instance=instance)
        if form.is_valid():
            # don't understand this line completely
            # many to many relationship
            instance.items.set(request.POST.get('items', ''))
            instance.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your menu has been succesfully updated!")
            return HttpResponseRedirect(reverse('menu:index'))
    return render(request, 'menu_detail.html', {'form': form})


def create_new_menu(request):
    form = forms.MenuForm()
    if request.method == 'POST':
        form = forms.MenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your menu has been succesfully created!")
            return HttpResponseRedirect(reverse('menu:index'))
    return render(request, 'menu_detail.html', {'form': form})


def delete_menu(request, pk):
    menu = models.Menu.objects.get(pk=pk)
    menu.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        "Menu has been sucessfully deleted!")
    return HttpResponseRedirect(reverse('menu:index'))


def add_ingredient(request):
    form = forms.IngredientForm()
    if request.method == 'POST':
        form = forms.IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Ingredient has been succesfully added!")
            return HttpResponseRedirect(reverse('menu:index'))
    return render(request, 'menu_detail.html', {'form': form})


def add_item(request):
    form = forms.ItemForm()
    if request.method == 'POST':
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Item has been succesfully added!")
            return HttpResponseRedirect(reverse('menu:index'))
    return render(request, 'menu_detail.html', {'form': form})
