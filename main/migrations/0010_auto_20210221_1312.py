# Generated by Django 3.1.2 on 2021-02-21 07:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20210221_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='group',
            field=models.ManyToManyField(null=True, to='main.Group'),
        ),
    ]
