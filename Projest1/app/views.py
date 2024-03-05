from django.shortcuts import render
from django.http import HttpResponse

def dif1(request):
    return render(request,'dif1.html')

def dif2(request):
    return render(request,'dif2.html')

def pack(request):
    return render(request,'packages.html')

def nav(request):
    return render(request,'commands.html')