from django.shortcuts import render
from .forms import CustomerDetailForm
from django.http import HttpResponse

def customer_details(request):
    if request.method == 'POST':
        form = CustomerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = CustomerDetailForm()
    return render(request, 'food_delivery_app/customer_details.html', {'form': form})
