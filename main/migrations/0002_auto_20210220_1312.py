# Generated by Django 3.1.2 on 2021-02-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='poll',
        ),
        migrations.AddField(
            model_name='poll',
            name='group',
            field=models.ManyToManyField(to='main.Group'),
        ),
    ]
