from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.menu_view, name='index'),
    path('menu/<int:pk>/', views.menu_detail, name='edit'),
]
