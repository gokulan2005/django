from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def n1(request):
    return HttpResponse('n1 fun')

def n2(request):
    return HttpResponse('n2 fun')
def n3(request):
    return HttpResponse('n3 fun')