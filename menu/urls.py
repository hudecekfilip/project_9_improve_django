from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.menu_view, name='index'),
    path('menu/<int:pk>/edit/', views.menu_detail, name='edit'),
    path('menu/new/', views.create_new_menu, name='create_new_menu'),
    path('menu/<int:pk>/delete/', views.delete_menu, name='delete'),
    path('menu/add/ingredient/', views.add_ingredient, name='add_ingredient'),
    path('menu/add/item/', views.add_item, name='add_item'),
]
