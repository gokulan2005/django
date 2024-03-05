# halls/forms.py
from django import forms
from .models import Hall, Department

class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
