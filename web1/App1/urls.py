from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('n1/', n1, name='index'),
    path('n2/', n2, name='index'),
    path('n3/', n3, name='index'),
    
    # Add other URL patterns as needed
]