# Generated by Django 3.0 on 2020-07-10 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_handle', '0002_auto_20200710_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]