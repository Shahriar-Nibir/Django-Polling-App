from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .decorators import *

# Create your views here.


@login_required(login_url='login')
def home(request):
    name = request.user
    groups = name.group_set.all()
    polls = Poll.objects.none()
    for group1 in groups:
        poll = Poll.objects.filter(group=group1)
        polls = polls | poll
    mypolls = Poll.objects.filter(created_by=name)
    context = {'polls': polls, 'mypolls': mypolls}
    return render(request, 'index.html', context)


@unauthenticated_user
def loginProc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def signup(request):
    form = CreateUser()
    context = {'forms': form}
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def poll(request, pk):
    poll = Poll.objects.get(id=pk)
    options = poll.option_set.all()
    context = {'options': options}
    return render(request, 'poll.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def group(request):
    form = GroupForm()
    context = {'form': form}
    if request.method == 'POST':
        f = GroupForm(request.POST)
        if f.is_valid:
            f.save()
            return redirect('createpoll')
    return render(request, 'group.html', context)


@login_required(login_url='login')
def createpoll(request):
    poll = Poll()
    user = request.user
    form = PollForm(instance=poll)
    context = {'form': form, 'poll': poll}
    if request.method == 'POST':
        f = PollForm(request.POST, instance=poll)
        if f.is_valid:
            temp = f.save(commit=False)
            temp.created_by = user
            temp.save()
            return redirect('addoptions', pk=poll.id)
        else:
            poll.delete()
    return render(request, 'createpoll.html', context)


@login_required(login_url='login')
def addoptions(request, pk):
    poll = Poll.objects.get(id=pk)
    OptionForm = modelformset_factory(
        Option, fields=('option_name',), extra=10)
    queryset = Option.objects.none()
    form = OptionForm(request.POST or None, queryset=queryset)
    context = {'form': form}
    if form.is_valid:
        instances = form.save(commit=False)
        for instance in instances:
            instance.poll = poll
            instance.save()
            return redirect('home')
    return render(request, 'addoptions.html', context)


@login_required(login_url='login')
def result(request, pk):
    poll = Poll.objects.get(id=pk)
    results = poll.option_set.all()
    context = {'results': results, 'poll': poll}
    return render(request, 'result.html', context)
