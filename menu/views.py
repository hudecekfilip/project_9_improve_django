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
            return HttpResponseRedirect(reverse('menu:index'))
    return render(request, 'menu_detail.html', {'form': form})
