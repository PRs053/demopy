# Generated by Django 4.2.2 on 2023-09-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-02-02'),
            preserve_default=False,
        ),
    ]
