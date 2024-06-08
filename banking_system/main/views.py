
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from main.models import Customer
from django.contrib.auth import logout
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('home')


def dashboard(request):
   if request.user.is_authenticated:
    user = request.user
    return render(request, 'home/dashboard.html', {'user': user})
   else:
     error="Login Required"
     messages.error(request, error)
     return redirect('login')
  

def home(request):
    return render(request, 'home/home.html')

def authenticat(username=None, password=None):
    try:
        print(username)
        user = Customer.objects.get(Customer_name=username)
        if user.password==password:
            return user
    except Customer.DoesNotExist:
        return None

def login_view(request):
    error = None
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticat(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')  
        else:
            error = 'Invalid username or password.'
    else:
        next_page = request.GET.get('next', '')
        return render(request, 'home/login.html', {'next': next_page})
    return render(request, 'home/login.html', {'error': error})