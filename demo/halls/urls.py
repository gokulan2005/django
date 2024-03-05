# halls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_hall/', views.add_hall, name='add-hall'),
    path('hall_list/', views.hall_list, name='hall-list'),
]
