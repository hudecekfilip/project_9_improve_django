from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from . import models
from . import forms

def menu_view(request):
    menus = models.Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})


def menu_detail(request, pk):
    instance = models.Menu.objects.get(pk=pk)
    form = forms.MenuForm(instance=instance)
    if request.method == 'POST':
        form = forms.MenuForm(request.POST, instance=instance)
        if form.is_valid():
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
