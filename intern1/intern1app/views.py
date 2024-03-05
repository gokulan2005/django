from django.shortcuts import render

from django.contrib.auth import authenticate, login
from flask import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard or any other page
        else:
            error_msg = 'Invalid username or password'
    else:
        error_msg = ''
    
    return render(request, 'intern1app/login.html', {'error_msg': error_msg})
