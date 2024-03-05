from django.urls import path
from .views import customer_details

urlpatterns = [
    path('', customer_details, name='customer_details'),
    # Add other URL patterns as needed
]