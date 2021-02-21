from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory, modelformset_factory
from .forms import *
from .models import *

# Create your views here.


def home(request):
    name = request.user
    groups = name.group_set.all()
    polls = Poll.objects.none()
    for group1 in groups:
        poll = Poll.objects.filter(group=group1)
        polls = polls | poll
    context = {'polls': polls}
    return render(request, 'index.html', context)


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


def poll(request, pk):
    poll = Poll.objects.get(id=pk)
    options = poll.option_set.all()
    context = {'options': options}
    return render(request, 'poll.html', context)


def confirm(request, pk):
    option1 = Option.objects.get(id=pk)
    user1 = request.user
    group = Group.objects.get(user=user1)
    if request.method == 'POST':
        option1.vote += 1
        option1.save()
        p1 = Choice()
        p1.save()
        p1.option.add(option1)
        p1.user.add(user1)
        p1.save()
        group.user.remove(user1)
        group.save()
        return redirect('home')
    context = {}
    return render(request, 'confirm.html', context)
