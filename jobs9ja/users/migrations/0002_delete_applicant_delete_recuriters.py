# Generated by Django 5.0.4 on 2024-06-20 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Applicant',
        ),
        migrations.DeleteModel(
            name='Recuriters',
        ),
    ]
