# Generated by Django 3.1.2 on 2021-03-11 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210311_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.poll'),
        ),
    ]
