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
        widgets = {
            'poll_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'user']

        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
