from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(requests):
    context={'name':'world'}
    return render(requests,'home.html',context)

def about(requests):
    context={'name':'about'}
    return render(requests,'about.html',context)

def studentList(requests):
    students= Student.objects.all()
    return render(requests,'students.html',{'student':students})

@login_required
def subscribe(requests):
    if requests.method == 'POST':
        email = requests.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(requests, 'You are already subscribed!')

        else:
            subscriber=Subscriber(email=email)
            subscriber.save()
            messages.success(requests, 'Thank you for subscribing!')    
            return redirect('subscribe')
    return render(requests, 'subscribe.html')

        
def add_pet(request):   
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES) 
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    
    return render(request, 'add_pet.html', {'form': form})


def pet_list(requests):
    pets = Pet.objects.all()
    return render(requests, 'pet_list.html', {'pets': pets})

def register(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribe')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})  
        
def login_form(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('subscribe')
        else:
            return render(request, 'login.html',{'error': 'Invalid credentials'})
        
    return render(request, 'login.html')
        

def logout_form(request):
     logout(request) 
     return redirect('log_in')  