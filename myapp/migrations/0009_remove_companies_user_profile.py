# Generated by Django 5.0.6 on 2024-07-22 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='user_profile',
        ),
    ]
