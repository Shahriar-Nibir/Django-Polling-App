# Generated by Django 3.1.2 on 2021-02-21 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210221_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='group',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.group'),
        ),
    ]