from django.shortcuts import render

# Create your views here.
def insta(request):
    return render(request, 'index.html')