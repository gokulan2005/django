from django.urls import path
from .views import *
urlpatterns = [
    path('3',dif1,name="dif1"),
    path('1',dif2,name="dif2"),
    path('2',pack,name="packages"),
    path('',nav,name="nav"),
]



