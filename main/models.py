from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=200, null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name


class Poll(models.Model):
    poll_name = models.CharField(max_length=200, null=True)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.poll_name


class Option(models.Model):
    option_name = models.CharField(max_length=200, null=True)
    vote = models.PositiveIntegerField(default=0, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.option_name+'-'+self.poll.poll_name


class Choice(models.Model):
    option = models.ManyToManyField(Option, null=True)
    user = models.ManyToManyField(User, null=True)
