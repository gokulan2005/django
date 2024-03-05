from django import forms
from .models import customer_details

class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = customer_details
        fields = ['name', 'email', 'phone', 'address', 'order_history', 'preferences']
