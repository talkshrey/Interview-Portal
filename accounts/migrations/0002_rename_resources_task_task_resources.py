# Generated by Django 4.0.3 on 2022-05-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='resources',
            new_name='task_resources',
        ),
    ]