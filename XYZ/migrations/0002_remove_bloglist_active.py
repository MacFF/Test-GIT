# Generated by Django 4.0.4 on 2023-11-03 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('XYZ', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglist',
            name='active',
        ),
    ]
