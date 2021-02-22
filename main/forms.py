from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['poll_name', 'description', 'group']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'user']
