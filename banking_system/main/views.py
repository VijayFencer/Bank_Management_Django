
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from main.models import Customer,Transaction
from django.contrib.auth import logout
from django.contrib import messages
from decimal import Decimal

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
            messages.success(request, 'Login successfully!')

            return redirect('dashboard')  
        else:
            error = 'Invalid username or password.'
    else:
        next_page = request.GET.get('next', '')
        return render(request, 'home/login.html', {'next': next_page})
    return render(request, 'home/login.html', {'error': error})


def update_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            phone_number = request.POST.get('phone_number')
            user = request.user
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.gender=gender
            user.phone_number=phone_number
            user.save()
            messages.success(request, 'Your details have been updated successfully!')
            return redirect('dashboard')

    else:
     error="Login Required"
     messages.error(request, error)
     return redirect('login')

def create_transaction(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sender_id = request.user.id
            receiver_id = request.POST.get('receiver_id')
            amount = Decimal(request.POST.get('amount'))

            sender = Customer.objects.get(id=sender_id)
            try:
                receiver = Customer.objects.get(id=receiver_id)
            except Customer.DoesNotExist:
                messages.error(request, 'Receiver not found.')
                return redirect('dashboard')  
            if sender.id==receiver.id:
                messages.error(request, 'Not possible to transfer for same account.')
                return redirect('dashboard')
            if receiver.id==1:
                messages.error(request, 'Not possible to transfer for this account.')
                return redirect('dashboard')
            if amount<100:
                messages.error(request, 'Minimum amount to transfer is 100.')
                return redirect('dashboard')       
            if sender.balance - amount >= 500:
                sender.balance -= amount
                sender.save()

                receiver.balance += amount
                receiver.save()

                transaction = Transaction.objects.create(
                    sender=sender,
                    receiver=receiver,
                    amount=amount
                )

                messages.success(request, f'Transaction completed successfully! {transaction}')
                return redirect('dashboard')  
            else:
                messages.error(request, 'Insufficient balance. Minimum balance of 500 must be maintained.')
                return redirect('dashboard')
    else:
        error="Login Required"
        messages.error(request, error)
        return redirect('login')


def trans_hist(request):
    if request.user.is_authenticated:
        user = request.user  
        sent_transactions = Transaction.objects.filter(sender=user)
        received_transactions = Transaction.objects.filter(receiver=user)
        
        transactions = sorted(
            list(sent_transactions) + list(received_transactions),
            key=lambda x: x.date,
            reverse=True
        )
        return render(request, 'home/dashboard.html', {'user': user,'transactions':transactions})
    else:
        error="Login Required"
        messages.error(request, error)
        return redirect('login')