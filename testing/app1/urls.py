from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='tag1'),
    # Add other URL patterns as needed
]