# Generated by Django 3.2.8 on 2022-06-18 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='scorecard',
        ),
        migrations.AddField(
            model_name='score',
            name='stack',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.applicationstack'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Scorecard',
        ),
    ]