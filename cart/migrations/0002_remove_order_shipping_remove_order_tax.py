# Generated by Django 5.0 on 2023-12-11 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
    ]
