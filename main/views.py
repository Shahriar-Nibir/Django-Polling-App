from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'index.html')


def loginProc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def signup(request):
    form = CreateUser()
    context = {'forms': form}
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    return render(request, 'signup.html', context)
