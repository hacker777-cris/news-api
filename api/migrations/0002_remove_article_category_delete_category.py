# Generated by Django 5.0.6 on 2024-07-07 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
