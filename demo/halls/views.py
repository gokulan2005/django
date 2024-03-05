# halls/views.py
from django.shortcuts import render, redirect
from .models import Hall, Department
from .forms import HallForm, DepartmentForm

def add_hall(request):
    if request.method == 'POST':
        form = HallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hall-list')
    else:
        form = HallForm()
    return render(request, 'halls/add_hall.html', {'form': form})

def hall_list(request):
    halls = Hall.objects.all()
    return render(request, 'halls/hall_list.html', {'halls': halls})
